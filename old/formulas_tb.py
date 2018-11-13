
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import datetime

import os
    
class DurationFundos(object):
    
    
    
    def __init__(self,data,dict_tp,dict_vna):
        self.data=data
        self.dict_tp=dict_tp
        self.dict_vna=dict_vna
        self.duration_carteiras(data,dict_tp,dict_vna)
        
        
        
    def duration_carteiras(self,data,dict_tp,dict_vna):
        import os
        from formulas_aux import dict_meses
        
        
        data="{0:0=2d}".format(data.day)+dict_meses.get(str(data.month))+str(data.year)
        path = os.getcwd()[:os.getcwd().find('Desktop')]

        arquivo = path+'Downloads\\AllTradingDesksOverView'+str(data)+'.txt'

        fundos= pd.read_csv(arquivo, sep='\t')










        fundos = fundos[(fundos['Fund']=='RIO BRAVO APOLLO FIM')|(fundos['Fund']=='RIO BRAVO JUROS MASTER FI RF')
                |(fundos['Fund']=='RIO BRAVO PREVIDENCIA FIM')]
        fundos = fundos[(fundos['Book']!='Despesas_FIM')&(fundos['Book']!='Caixa_Aplicação')&(fundos['Book']!='Caixa_Offshore')
           &(fundos['Book']!='Caixa_Transfer')&(fundos['Book']!='Despesas_FIM')].reset_index(drop=True).fillna(0.0)







        dict_nomes={
            fundos.columns[0]:'date',
            fundos.columns[1]:'fundo',
            fundos.columns[2]:'ativo',
            fundos.columns[3]:'classe_ativo',
            fundos.columns[4]:'book',
            fundos.columns[5]:'vencimento',
            fundos.columns[6]:'pu_financeiro',
            fundos.columns[7]:'pu',
            fundos.columns[8]:'financeiro_anterior',
            fundos.columns[9]:'pu_anterior',
            fundos.columns[11]:'posicao_atual',
            fundos.columns[12]:'pl',
            fundos.columns[13]:'quantidade',
            fundos.columns[14]:'quantidade_anterior',
            fundos.columns[15]:'exposicao_cambial',
            fundos.columns[16]:'exposicao_juros',
            fundos.columns[17]:'exposicao_equity',
        }
        fundos.rename(columns=dict_nomes, inplace=True)



        fundos=fundos[['date','fundo','ativo','classe_ativo','book','vencimento','pu_financeiro','pu','financeiro_anterior',
                       'pu_anterior', 'posicao_atual','pl','quantidade','quantidade_anterior','exposicao_cambial','exposicao_juros',
                       'exposicao_equity']]


        fundos[['date','vencimento']]=fundos[['date','vencimento']].apply(pd.to_datetime,errors='coerce')
        fundos[['pu_financeiro','pu','financeiro_anterior','pu_anterior','posicao_atual','pl','quantidade_anterior']]=fundos[['pu_financeiro',
                'pu','financeiro_anterior','pu_anterior','posicao_atual','pl','quantidade_anterior']].apply(pd.to_numeric,errors='coerce')

        fundos=fundos[(fundos['classe_ativo']=='LTN')|(fundos['classe_ativo']=='NTN-B')|(fundos['classe_ativo']=='LFT')|
                       (fundos['classe_ativo']=='NTN-F')].reset_index(drop=True)
        
        return fundos

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def titulos(data,vencimento,taxa,resultado='pu',cupom=0.06,valor_futuro=1000,vna=1):
    from helper import feriados
    feriados = list(feriados.lista())
    if cupom == 0.0:
        du = np.busday_count(data,vencimento,holidays=feriados)/252.0
        pu = valor_futuro/(1+taxa)**du
        mod = du
    else:
        dt_cupom = vencimento
        lst=[]
        cupom  = ((1+cupom)**(0.5)-1)*valor_futuro*vna
        while dt_cupom >= data:
            mes = dt_cupom.month-6
            ano = dt_cupom.year
            if mes < 0:
                mes+=12
                ano=dt_cupom.year - 1
            dt_cupom = pd.to_datetime(str(ano) + '-' + str(mes) +'-' + str(vencimento.day))
            lst.append({'datas_cupom':dt_cupom})
        lst.append({'datas_cupom':vencimento})
        df=pd.DataFrame.from_dict(lst)
        df=df[df['datas_cupom']>data].sort_values(by='datas_cupom', ascending=True).reset_index(drop=True)
        df['dia']=data
        df['du']=np.busday_count(list(df['dia'].copy()),list(df['datas_cupom'].copy()),holidays=feriados)/252.0
        df['fator']=1/(1+float(taxa))**df['du']
        df['valor_de_face']=df['fator']*cupom
        pu=df['valor_de_face'].sum() + df['fator'].min()*valor_futuro*vna
        df['fator_mod']=((df['du']*cupom)/(1+float(taxa))**df['du'])/pu
        mod = df['fator_mod'].sum() + df['fator'].min()*valor_futuro/pu
    if resultado == 'pu':
        return pu
    else:
        return mod
    
    
    
    
def cupons(data,vencimento):
    from helper import feriados
    feriados = list(feriados.lista())
    dt_cupom = vencimento
    lst=[]
    while dt_cupom >= data:
        mes = dt_cupom.month-6
        ano = dt_cupom.year
        if mes < 0:
            mes+=12
            ano=dt_cupom.year - 1
        dt_cupom = pd.to_datetime(str(ano) + '-' + str(mes) +'-' + str(vencimento.day))
        lst.append({'datas_cupom':dt_cupom})
    return lst