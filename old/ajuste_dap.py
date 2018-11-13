
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import datetime
from helper import feriados

feriados = list(feriados.lista())

class Ajustes_dap(object):
 

    def __init__(self, arcv):
        self.arcv = arcv
        
    def result(self):
        arcv = self.arcv
        d = pd.read_excel(arcv, header=1,sheetname ='base_dados',skip_footer=1)\
                    .fillna(method='ffill', limit=2).fillna(0.0).reset_index(drop=True)
        i=0
        while i+2<=len(d.columns):
            try:
                df
            except:
                df=d[d.columns[i:i+2]].copy()
                df['ticker'] = df.columns[1]
                df.rename(columns={
                    df.columns[0]:'data',
                    df.columns[1]:'preco',
                },inplace=True)
                i+=2
            else:
                dn=d[d.columns[i:i+2]].copy()
                dn['ticker'] = dn.columns[1]
                dn.rename(columns={
                    dn.columns[0]:'data',
                    dn.columns[1]:'preco',
                },inplace=True)
                df=pd.concat([df,dn])
                i+=2
                
        df=df[df['data']!=pd.to_datetime(0)].reset_index(drop=True)
        df['ativo']=[ativo(df['ticker'][i]) for i in df.index]
        df['vencimento']=[vencimento(df['ticker'][i],df['ativo'][i]) for i in df.index]
        
        return df
    def tickers(self, df):
        tickers = df[['ativo','ticker','vencimento']].copy().drop_duplicates(subset=['ticker','vencimento']).reset_index(drop=True)
        return tickers
        

venc={
    'F':'01',
    'G':'02',
    'H':'03',
    'J':'04',
    'K':'05',
    'M':'06',
    'N':'07',
    'Q':'08',
    'U':'09',
    'V':'10',
    'X':'11',
    'Z':'12'
}
dia={
    'DAP':'15',
    'NTNB':'15',
    'DI1':'01'
}

def vencimento(ticker,ativo):
    if ativo=='NTNB':
        v = pd.to_datetime(ticker.split()[1], format='%d/%m/%Y')
    else:
        v = pd.to_datetime(dia[ativo]+'/'+venc[ticker[3]]+'/20'+ticker[-2:], format='%d/%m/%Y')
    return v    

def ativo(ticker):
    if len(ticker)==6:
        a = ticker[0:3]
    else:
        a = 'NTNB'
    return a

def tickers_juros_real(vencimento, tickers):
    '''Esta função retorna quais são os DIs necessários para interpolar a taxa de um DAP/NTN-B qualquer. O imput é o vencimento
    do DAP/NTN-B e o output são os tickers dos DIs que serão utilizados'''
    
    di = tickers[tickers['ativo']=='DI1'].reset_index(drop=True)
    i = (di[di['vencimento']>vencimento].head(1).index-1).tolist()[0]
    return di.iloc[i:i+2].reset_index(drop=True)


def interpol_juros_nominal(df, vencimento, tickers):

    dt=df[(df['ticker']==tickers_juros_real(vencimento,tickers)['ticker'][0])|\
       (df['ticker']==tickers_juros_real(vencimento,tickers)['ticker'][1])|\
         ((df['ativo']=='DAP')&(df['vencimento']==vencimento))].copy().reset_index(drop=True)
    
    dt['networkdays']=[np.busday_count(pd.to_datetime(dt['data'][i]),pd.to_datetime(dt['vencimento'][i]),holidays=feriados)\
                 for i in dt.index]
    dt['data_intermed']=[np.busday_count(pd.to_datetime(dt['data'][i]),vencimento,holidays=feriados)\
                 for i in dt.index]
    pvt = pd.pivot_table(dt, values=['preco','networkdays','data_intermed'], index='data', columns='ticker')
    
    p1 = (1+pvt['preco'][pvt['preco'].columns[1]]/100)**(pvt['networkdays'][pvt['networkdays'].columns[1]]/252)
    p2 = (1+pvt['preco'][pvt['preco'].columns[2]]/100)**(pvt['networkdays'][pvt['networkdays'].columns[2]]/252)
    dif = ((pvt['data_intermed'][pvt['data_intermed'].columns[1]]/252) - (pvt['networkdays'][pvt['networkdays'].columns[1]]/252))/\
            ((pvt['networkdays'][pvt['networkdays'].columns[2]]/252) - (pvt['networkdays'][pvt['networkdays'].columns[1]]/252))
    laddir = p1 * ((p2/p1)**dif)
    pvt=pvt.dropna()
    pvt['juros_nominal']=((laddir**(1/(pvt['data_intermed'][pvt['data_intermed'].columns[1]]/252)))-1)*100
    pvt['juros_real'] = (((1+pvt['juros_nominal']/100)/(1+pvt['preco'][pvt['preco'].columns[0]]/100))-1)*100
    
    pvt=pvt[['preco','juros_nominal','juros_real']].drop([pvt['preco'].columns[1],pvt['preco'].columns[2]],level='ticker',axis=1)
    pvt.rename(columns={
                    'preco':pvt['preco'].columns[0],
                },inplace=True)
    
    pvt = pvt.unstack().reset_index().drop('ticker',1).rename(columns={
                                                                'level_0':'curva',
                                                                0:'taxa'
                                                            })
    pvt = pd.pivot_table(pvt, values=['taxa'], index='data', columns='curva')['taxa']
    return pvt



