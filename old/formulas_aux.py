
# coding: utf-8
import numpy as np

#Fórmulas de FRC
def PU(taxa, anos, ajuste=10000.0, vf=100000.0, ponto=0.5):
    return (vf*ponto)/(1+taxa/ajuste*anos)


def taxa_frc(PU, anos, ajuste=1, vf=100000.0, ponto=0.5):
    return (vf*ponto/PU-1)/anos



#Estatísticas
def vol_diaria(df_cotas, coluna='cota'):
    m252 = np.sqrt(252)
    df = df_cotas.copy()
    df['retorno'] = np.log(df[coluna].pct_change() + 1)
    return df.retorno.std() * m252


def rolling_vol(df_cotas, janela=126, coluna='cota'):
    '''
    Janela= valor em dias uteis
    '''
    m252 = np.sqrt(252)
    df = df_cotas.copy()
    df['retorno'] = np.log(df[coluna].pct_change() + 1)
    df['rolling_vol'] = df.retorno.rolling(window=janela).std() * m252
    return df


def drawdown(df_cotas, coluna='cota'):
    df = df_cotas.copy()
    df['drawdown'] = (df[coluna] / df[coluna].expanding().max()) - 1
    print min(df.drawdown)
    return df


def retorno_anualizado(df_cotas, coluna='cota'):
    return (df_cotas[coluna].values[-1] / df_cotas[coluna].values[0]) ** (252.0 / len(df_cotas[coluna].values)) - 1


def rolling_return(df_cotas, coluna=['cota'], janela=252):
    df = df_cotas.copy()
    for c in coluna:
        df['retorno_anualizado_{0}'.format(c)] = (df[c].pct_change(janela) + 1) ** (252.0 / janela) - 1
    df = df.dropna()
    return df

def rolling_vol_pt(df, coluna, janela=21):
    m252 = np.sqrt(252)
    df = df.copy
    df['rolling_vol_pt']=df[coluna].rolling(window=janela).std()*m252
    return df



dict_meses={
    '1':'Jan',
    '2':'Feb',
    '3':'Mar',
    '4':'Apr',
    '5':'May',
    '6':'Jun',
    '7':'Jul',
    '8':'Aug',
    '9':'Sep',
    '10':'Oct',
    '11':'Nov',
    '12':'Dec'
}