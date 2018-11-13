import datetime
import pandas as pd
import numpy as np


class TaxasHistoricas(object):
    def __init__(self, preco_frc,lst_dias=None):
        self.preco_frc=preco_frc
        self.lst_dias=lst_dias
        self.ajuste_dados()
        
    def ajuste_dados(self):
        preco_frc=self.preco_frc
        lst_dias=self.lst_dias

        preco_frc = preco_frc.drop_duplicates(subset=['date','sequencia_vencimento_futuro']).sort_values(by=['sequencia_vencimento_futuro','date']).reset_index(drop=True).copy()
        preco_frc['date'] = pd.to_datetime(preco_frc['date'])
        preco_frc['data_limite_negociacao'] = pd.to_datetime(preco_frc['data_limite_negociacao'])
        preco_frc['data_liquidacao_financeira'] = pd.to_datetime(preco_frc['data_liquidacao_financeira'])
        preco_frc['qtd_limt'] = (pd.to_timedelta(preco_frc['data_limite_negociacao'])-pd.to_timedelta(preco_frc['date'])).dt.days/360
        preco_frc['qtd_liqd'] = (pd.to_timedelta(preco_frc['data_liquidacao_financeira'])-pd.to_timedelta(preco_frc['date'])).dt.days/360
        preco_fut = preco_frc.drop(preco_frc[['codigo','ticker','preabe','premin','premax','premed','preult']],1)
#        
        if lst_dias==():
            qt_dias = preco_fut[preco_fut['date']==preco_fut['date'].max()].reset_index().copy()
            qt_dias['hoje']=pd.to_datetime(datetime.date.today())
            qt_dias['liq']=(pd.to_timedelta(qt_dias['data_liquidacao_financeira'])-pd.to_timedelta(qt_dias['hoje'])).dt.days

            lst_dias=qt_dias['liq'].tolist()
#
        
        
        
        pvt = pd.pivot_table(preco_fut, values=['cotacao_ajuste','qtd_liqd'],
                             index='date', columns='sequencia_vencimento_futuro')
        pvt['cotacao_ajuste']= np.where(pvt['cotacao_ajuste']==0,np.nan,pvt['cotacao_ajuste'])
        pvt = pvt.fillna(method='ffill')
        pvt['cotacao_ajuste']=pvt['cotacao_ajuste']/10000


        lst_nomes=[]
        lst_desloc=[]
        for dias in lst_dias:
            if dias/360.0<pvt['qtd_liqd'][pvt['qtd_liqd'].columns.min()].max():
                lst_desloc.append('Dias {0}'.format(dias) + \
                                  ' menor que o minimo. Deslocamento de {0}'.format(pvt['qtd_liqd'][pvt['qtd_liqd'].columns.min()].max()*360.0-dias)+ \
                                  ' dias')
                dias=pvt['qtd_liqd'][pvt['qtd_liqd'].columns.min()].max()*360.0
            elif dias/360.0>pvt['qtd_liqd'][pvt['qtd_liqd'].columns.max()].min():
                lst_desloc.append('Dias {0}'.format(dias) + \
                                  ' maior que o maximo. Deslocamento de {0}'.format(dias-pvt['qtd_liqd'][pvt['qtd_liqd'].columns.max()].min()*360.0) + \
                                  ' dias')
                dias=pvt['qtd_liqd'][pvt['qtd_liqd'].columns.max()].min()*360.0
            
            pvt['vencimento_1'],pvt['vencimento_2']=vencimento_search(pvt['qtd_liqd'],dias/360.0)
            pvt['taxa_interpolada_{0}'.format(dias)]=interpolacao(pvt,pvt['vencimento_1'],pvt['vencimento_2'],dias/360.0)
            lst_nomes.append('taxa_interpolada_{0}'.format(dias))

        df = pvt[lst_nomes].copy()
        
        print lst_desloc
        return df, lst_nomes, lst_desloc

    
class estoque_swap(object):
    
    
    def __init__(self, tb_scs):
        self.tb_scs=tb_scs
        self.contratos_abertos()
        self.cct_hist()
        
    def contratos_abertos(self):
        tb_scs = self.tb_scs
        
        estoque_aberto=tb_scs[['date','data_liquidacao_financeira','codigo','volume_uss','qtd_contratos_aberto',
       'qtd_contratos_negociados_dia']].sort_values(by='date').copy()
        estoque_aberto['qtd_contratos_aberto']=np.where(estoque_aberto['codigo']=='SCC',
                                                 estoque_aberto['qtd_contratos_aberto']*-1.0,estoque_aberto['qtd_contratos_aberto'])
        estoque_aberto['qtd_contratos_aberto']=estoque_aberto['qtd_contratos_aberto']/20.0
        
        estoque_atual = estoque_aberto[estoque_aberto['date']==estoque_aberto['date'].max()].sort_values('data_liquidacao_financeira').drop_duplicates()
        
        return estoque_aberto, estoque_atual
    
    def cct_hist(self):
        estoque_aberto,estoque_atual = self.contratos_abertos()
        pvt_hist = pd.pivot_table(estoque_aberto, values=['qtd_contratos_aberto'],
                     index='date', columns='data_liquidacao_financeira')
        pvt_hist=pvt_hist.fillna(0)
        
        return pvt_hist
    
    
    
    
    

    
def interpol(i1, t1, i2, t2, tn):
    p1 = (1+i1)**t1
    p2 = (1+i2)**t2
    ddiff = (tn-t1)/(t2-t1)
    
    
    laddir = p1 * ((p2/p1)**ddiff)
    return (laddir**(1/tn))-1



def vencimento_search(pvt, dias):
    for i in range(0,len(pvt)):
        df_dias=pd.DataFrame.transpose(pvt[pvt.index==pvt.index[i]]-dias)
        df_desloc=pd.DataFrame.transpose( pvt[pvt.index==pvt.index[i]].shift(-1,freq=None,axis=1)-dias)
        df_bool=(df_dias<0.0)&(df_desloc>0.0)
        for j in range(0, len(df_bool)):
            if df_bool.iloc[j].any()==True:
                return (j+1),(j+2)
                break
                
                
def interpolacao(pvt, vencimento_curto,vencimento_longo, dias):
    for i in range(0,len(pvt)):
        a=vencimento_curto.iloc[i]
        b=vencimento_longo.iloc[i]
        
        return interpol(pvt['cotacao_ajuste'][a],pvt['qtd_liqd'][a],
                       pvt['cotacao_ajuste'][b],pvt['qtd_liqd'][b],dias)