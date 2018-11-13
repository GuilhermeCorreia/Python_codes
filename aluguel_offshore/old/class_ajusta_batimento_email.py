
# coding: utf-8

import os
import sys
sys.path.append('%s/../' % os.getcwd())

import datetime
import pandas as pd
import numpy as np
import getpass

class AjustaBatimentoEmailCayman(object):
    '''Class destinada a fazer o último batimento das informações de Aluguel Ofshore - insumo vem dos e-mails de cayman'''
    
    def __init__(self, path):
        self.path = path
        
    def ajuste_dados_email(self, info_emails, abertura_batidos):
        
        ajuste = pd.merge(abertura_batidos.groupby(by=['acc', 'currency']).sum().reset_index(),                                              info_emails, on=['acc','currency'], how='left')
        
        check_10 = ajuste[ajuste['accrual_final_y'].isnull()==True].shape[0]
        print('%s linhas foram dropadas da base, porque os valores não foram descontados no conta.' %check_10) 
        ajuste['multiplicador'] = ajuste['accrual_final_y']/ajuste['accrual_final_x']
        ajuste = ajuste.rename(columns={
            'accrual_final_x':'accrual_final_gerado',
            'accrual_final_y':'accrual_final_email' 
        }).fillna(0).drop(['quantidade_book','accrual_final_gerado', 'accrual_final_email'], axis=1)
        
        abertura_batidos_ajustado = pd.merge(abertura_batidos, ajuste, on=['acc','currency'], how='left')
        check_11 = abertura_batidos_ajustado.shape[0]-abertura_batidos.shape[0]
        if check_11 != 0:
            print ('%s linhas foram duplicadas durante o ajuste. Verificar!!')
        abertura_batidos_ajustado['accrual'] = abertura_batidos_ajustado['accrual_final']                                                                *abertura_batidos_ajustado['multiplicador']
        abertura_batidos_ajustado = abertura_batidos_ajustado.drop(['accrual_final','multiplicador'], axis=1)
        
        check_12 = abertura_batidos_ajustado.shape[0]-abertura_batidos_ajustado[abertura_batidos_ajustado['accrual']!=0].shape[0]
        print('%s tickers_book foram dropados da abertura porque suas contas não faziam sentido com o que foi cobrado' %check_12)
        
        abertura_batidos_ajustado = abertura_batidos_ajustado[abertura_batidos_ajustado['accrual']!=0]
        abertura_batidos_ajustado_neg = abertura_batidos_ajustado[abertura_batidos_ajustado['accrual']<0]
        abertura_batidos_ajustado_posi = abertura_batidos_ajustado[abertura_batidos_ajustado['accrual']>=0]
        ajuste_neg_grouped = abertura_batidos_ajustado_neg.groupby(by=['acc','currency']).sum().reset_index()
        
        check_13 = abertura_batidos_ajustado_neg.shape[0]-                    pd.merge(abertura_batidos_ajustado_neg, ajuste_neg_grouped, on=['acc','currency'], how='left').shape[0]
        if check_13 != 0:
            print ('%s linhas foram duplicadas durante o ajuste dos números negativos. Verificar!!' %check_13)
            
        abertura_batidos_ajustado_neg = pd.merge(abertura_batidos_ajustado_neg, ajuste_neg_grouped, on=['acc','currency'], how='left')
        abertura_batidos_ajustado_neg['pct'] = abertura_batidos_ajustado_neg['accrual_x']/abertura_batidos_ajustado_neg['accrual_y']
        
        check_14 = abertura_batidos_ajustado_neg.groupby(by=['acc','currency']).sum().reset_index()
        check_14 = check_14[np.isclose(check_14['pct'], 1)==False].shape[0]
        if check_14 != 0:
            print ('O batimento não foi feito!!! %s contas somam valor diferente a 100\%')
        
        abertura_batidos_ajustado_posi = abertura_batidos_ajustado_posi.groupby(by=['acc','currency']).sum().reset_index()
        check_15 = abertura_batidos_ajustado_neg.shape[0]-                                    pd.merge(abertura_batidos_ajustado_neg, abertura_batidos_ajustado_posi,                                                          on=['acc','currency'], how='left').shape[0]
        if check_15 != 0:
            print ('%s linhas foram duplicadas durante o ajuste de quantidades positivas!!!'%check_15)
            
        abertura_batidos_ajustado_neg = pd.merge(abertura_batidos_ajustado_neg, abertura_batidos_ajustado_posi,                                          on=['acc','currency'], how='left').fillna(0)
        abertura_batidos_ajustado_neg['distrib_positives'] = abertura_batidos_ajustado_neg['pct']                                                        *abertura_batidos_ajustado_neg['accrual']
        abertura_batidos_ajustado_neg['accrual_final'] = abertura_batidos_ajustado_neg['accrual_x']+                                                        abertura_batidos_ajustado_neg['distrib_positives']
        abertura_batidos_ajustado = abertura_batidos_ajustado_neg.drop(['accrual_x', 'accrual_y', 'pct', 'accrual', 
                                                          'distrib_positives'], axis=1)    
        abertura_batidos_consol = abertura_batidos_ajustado.groupby(['acc', 'book', 'currency'])                                        .sum().reset_index().drop(['quantidade_book','quantidade_book_y'], axis=1)                                                .rename(columns={'quantidade_book_x':'quantidade_book'})
                
        check_16 = pd.merge(abertura_batidos_ajustado.groupby(by=['acc', 'currency']).sum().reset_index(),                                     info_emails, on=['acc','currency'],how='left')
        check_16['pct'] = check_16['accrual_final_x']/check_16['accrual_final_y']
        check_16 = check_16[np.isclose(check_16['pct'], 1)==False].shape[0]
        if check_16 != 0:
            print ('O batimento não foi feito!!! %s contas somam valor diferente a 100\%')
            
        abertura_batidos_ajustado[abertura_batidos_ajustado.book=='LOCAL_ADR_INTC'][['conta','agent','data_ref','quantidade_book_x',
                                                                             'book', 'ticker','currency','accrual_final']].to_excel('LOCAL_ADR_INTC.xlsx')
        
        return abertura_batidos_ajustado, abertura_batidos_consol, ajuste




