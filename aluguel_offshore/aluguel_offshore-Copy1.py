# coding: utf-8

import os
import sys
sys.path.append('%s/../' % os.getcwd())

import datetime
import pandas as pd
import numpy as np

class ImportAluguelOffshore(object):
    
    def __init__(self, pasta,data_inicio,data_final):
        self.pasta= pasta
        self.data_inicio = data_inicio
        self.data_final = data_final
    
    def povoa_lista_files(self):
        print('Povoando lista de arquivos que serão baixados para a memória')
        data_inicio = self.data_inicio
        data_final =  self.data_final
        lista_files = []
        pasta = self.pasta
        for file in os.listdir(pasta):
            data = pega_data_file(file)

            try:
                if (data>=data_inicio)&(data<=data_final):
                    lista_files.append(pasta+'\\'+file)
            except TypeError:
                print ('    O arquivo %s não pôde ser comparado com os demais' %(file))
        
        print('--------------------------------------------------------------------------------------------------------------')
        return lista_files
    
    def baixa_dados_df(self):
        lista_files = self.povoa_lista_files()
        pasta = self.pasta
        ubs_count=0
        morgan_count=0
        pras_count=0
        bdwm_count=0
        intc_count=0
        print('Baixando arquivos!!')
        for file in lista_files:
            if 'Ajuste' in file:
                data = file[-14:-4]
                try:
                    ubs
                except:
                    ubs = pd.read_csv(file)
                    ubs['date']=data
                else:
                    ubs_1 = pd.read_csv(file)
                    ubs_1['date']=data
                    ubs = pd.concat([ubs,ubs_1], axis=0)
                ubs_count+=1

            elif 'PROP+ASSET' in file:
                try:
                    pras
                except:
                    pras = pd.read_excel(file)
                    pras['date'] = pras.columns[7]
                    pras = pras.rename(columns={pras.columns[7]:'shares'})
                else:
                    pras_1 = pd.read_excel(file)
                    pras_1['date'] = pras_1.columns[7]
                    pras_1 = pras_1.rename(columns={pras_1.columns[7]:'shares'})
                    pras = pd.concat([pras,pras_1], axis=0)

                pras_count+=1

            elif 'Aluguel INT C' in file:
                try:
                    intc
                except:
                    intc = pd.read_excel(file)
                    intc['date'] = intc.columns[7]
                    intc = intc.rename(columns={intc.columns[7]:'shares'})
                else:
                    intc_1 = pd.read_excel(file)
                    intc_1['date'] = intc_1.columns[7]
                    intc_1 = intc_1.rename(columns={intc_1.columns[7]:'shares'})
                    intc = pd.concat([intc,intc_1], axis=0)

                intc_count+=1

            elif 'Clients BD+WM' in file:
                try:
                    bdwm
                except:
                    bdwm = pd.read_excel(file)
                    bdwm['date'] = bdwm.columns[31]
                    bdwm = bdwm.rename(columns={bdwm.columns[31]:'shares'})
                else:
                    bdwm_1 = pd.read_excel(file)
                    bdwm_1['date'] = bdwm_1.columns[31]
                    bdwm_1 = bdwm_1.rename(columns={bdwm_1.columns[31]:'shares'})
                    bdwm = pd.concat([bdwm,bdwm_1], axis=0)

                bdwm_count+=1

            elif ('038CDBD08_IN150DX' in file)|('038CDB895_IN150DX' in file):
                try:
                    morgan
                except:
                    morgan = pd.read_csv(file, skipfooter=1, engine='python')
                else:
                    morgan_1 = pd.read_csv(file, skipfooter=1, engine='python')
                    morgan = pd.concat([morgan, morgan_1], axis = 0)

                morgan_count+=1

        print('    ' + str(ubs_count) + ' arquivos do ubs importados')
        print('    ' + str(morgan_count) + ' arquivos da morgan importados')
        print('    ' + str(pras_count) + ' arquivos do Calypso PROP+ASSET importados')
        print('    ' + str(bdwm_count) + ' arquivos do Calypso BD+WM importados')
        print('    ' + str(intc_count) + ' arquivos do Calypso INTC importados')
        
        print('--------------------------------------------------------------------------------------------------------------')
        return ubs, morgan, intc, bdwm, pras
    
    
    def ajusta_tabelas_ubs(self, ubs):
        ubs['date'] = pd.to_datetime(ubs['date'], format='%Y-%m-%d')
        ubs['date'] = np.where(ubs['date'].dt.weekday==6, ubs['date']-datetime.timedelta(2), ubs['date'])
        ubs['pb'] = 'ubs'
        ubs['month_number'] = ubs['date'].dt.month
        ubs['year'] = ubs['date'].dt.year
        ubs['month'] = ubs['month_number'].map(months_dict)
        ubs['cusip'] = np.nan
        ubs = ubs[['Reference Account Id' ,'pb', 'date', 'Ticker', 'ISIN', 'cusip', 'SEDOL', 'Quantity',
                   'Daily Accrual', 'Billing CCY', 'month', 'year']].drop_duplicates()
        ubs.columns = ['conta', 'pb', 'data_ref', 'ticker', 'isin', 'cusip', 'sedol', 'qt', 'accrual', 'currency', 'month', 'year']
        ubs = ubs.drop_duplicates(subset=['conta', 'data_ref', 'ticker', 'qt', 'currency'])
        ubs = ubs[ubs['conta'].isnull()==False]
        
        return ubs
    def ajusta_tabelas_morgan(self, morgan):
        morgan['date'] = pd.to_datetime(morgan['Value Date'], errors='coerce', format = '%m/%d/%Y')
        morgan['pb'] = 'ms'
        morgan['month_number'] = morgan['date'].dt.month
        morgan['year'] = morgan['date'].dt.year
        morgan['month'] = morgan['month_number'].map(months_dict)
        morgan = morgan[['Account', 'pb', 'date', 'Symbol', 'ISIN', 'Cusip', 'Sedol', 'Shares', 'Net Borrow Cost', 'Currency', 'month', 'year']] 
        morgan.columns = ['conta', 'pb', 'data_ref', 'ticker', 'isin', 'cusip', 'sedol', 'qt', 'accrual', 'currency', 'month', 'year']  
        nparray = np.where(morgan['data_ref'].dt.weekday==6, morgan['data_ref']-datetime.timedelta(2),morgan['data_ref'])
        morgan = morgan.drop('data_ref', axis=1)
        morgan['data_ref'] = nparray
        morgan = morgan.drop_duplicates().reset_index(drop=True) 
        morgan = morgan[morgan['conta'].isnull()==False]
        
        return morgan
    
    def ajusta_tabelas_pb(self, ubs, morgan):
        ubs = self.ajusta_tabelas_ubs(ubs)
        morgan = self.ajusta_tabelas_morgan(morgan)
        pb = pd.concat([morgan, ubs], axis=0).reset_index(drop=True)
        pb.qt = (pb.qt.replace( '[)]','', regex=True )
                   .replace( '[(]','-',   regex=True ).astype(float))    
        pb.accrual = (pb.accrual.replace( '[)]','', regex=True )
                   .replace( '[(]','-',   regex=True ).astype(float))
        pb['qt'] = -abs(pb['qt'])
        pb['accrual'] = -abs(pb['accrual'])
        pb = pb[pb.data_ref.dt.weekday<5]
        #Como estamos pegando somente os dias úteis, multiplica o valor de sexta por 3 para levar em consideração dias corridos
        nparray = np.where(pb.data_ref.dt.weekday==4, pb['accrual']*3, pb['accrual'])
        pb['accrual'] = nparray
        contas =  pb['conta'].astype(str).copy()
        pb['conta'] = contas
        #Aplica o dicionário de contas que também está no aluguel_offshore.py
        pb['acc'] = pb['conta'].apply(lambda x: dict_contas[x])
        pb = pb[['conta', 'pb', 'data_ref', 'ticker', 'isin', 'cusip','sedol','qt', 'accrual','currency','month','year']]
       
        return pb
    
    def ajusta_tabelas_calypso(self, pras, bdwm, intc):
        pras['tipo'] = 'ASSET'
        bdwm['tipo'] = 'WM'
        intc['tipo'] = 'INT C'
        calypso = pd.concat([pras, bdwm, intc], axis=0).reset_index(drop=True)    
        calypso['date'] = pd.to_datetime(calypso['date'])
        calypso['month_number'] = calypso['date'].dt.month
        calypso['year'] = calypso['date'].dt.year
        calypso['month'] = calypso['month_number'].map(months_dict)
        calypso = calypso[['Account Name','tipo', 'Agent','date', 'shares', 'Book', 'PRODUCT_CODE.TICKER', 'PRODUCT_CODE.ISIN', 
                           'PRODUCT_CODE.CUSIP', 'Underlying.Product Code.SEDOL', 'Product Currency', 'month', 'year']].reset_index(drop=True)
        calypso.columns = ['conta_pb','conta', 'agent', 'data_ref', 'quantidade', 'book', 'ticker', 'isin', 'cusip', 'sedol',
                           'currency', 'month', 'year']
        calypso.conta_pb = calypso.conta_pb.astype(str)
        calypso = calypso[calypso.data_ref.dt.weekday<5]
        calypso_1 = calypso.copy()
        calypso_1['acc'] = calypso_1['conta_pb'].map(dict_contas)
        #Pega somente os arquivos do calypso que se referem às contas da asset
        calypso = calypso[calypso.conta_pb.isin(dict_contas.keys())].copy() #ESSA É A LINHA QUE EU VOU TER QUE ALTERAR PRA N DPAR ACCS
        calypso['quantidade'] = calypso['quantidade'].replace(',','', regex=True)
        calypso['quantidade'] = calypso['quantidade'].astype(float)
        
        return calypso, calypso_1
    def tabelas_ajustadas(self, ubs, morgan, pras, bdwm, intc):
        pb = self.ajusta_tabelas_pb(ubs, morgan)
        calypso, calypso_1 = self.ajusta_tabelas_calypso(pras, bdwm, intc)
        
        return pb, calypso, calypso_1
    
    def ajusta_calypso_wm(self, pb_wm, bdwm):
        calypso_wm = bdwm.copy()
        calypso_wm['tipo'] = 'WM' 
        calypso_wm['date'] = pd.to_datetime(calypso_wm['date'])
        calypso_wm['month_number'] = calypso_wm['date'].dt.month
        calypso_wm['year'] = calypso_wm['date'].dt.year
        calypso_wm['month'] = calypso_wm['month_number'].map(months_dict)
        calypso_wm = calypso_wm[['Account Name','tipo', 'Agent','date', 'shares', 'Book', 'PRODUCT_CODE.TICKER', 'PRODUCT_CODE.ISIN', 
                           'PRODUCT_CODE.CUSIP', 'Product Currency', 'month', 'year', 'LE Name']].reset_index(drop=True)
        calypso_wm.columns = ['conta_pb','conta', 'agent', 'data_ref', 'quantidade', 'book', 'ticker', 'isin', 'cusip', 
                      'currency', 'month', 'year', 'cliente']
        calypso_wm['quantidade'] = calypso_wm['quantidade'].replace(',','', regex=True)
        calypso_wm['quantidade'] = calypso_wm['quantidade'].astype(float)
        calypso_wm['quantidade'] = -1*calypso_wm['quantidade']
        calypso_wm = calypso_wm[calypso_wm['quantidade']<0]
        calypso_wm = calypso_wm[calypso_wm['currency']!='CLP']
        
        calypso_wm_grouped =calypso_wm.groupby(by=['data_ref', 'book', 'ticker', 'currency']).sum().reset_index()
        
        check = pb_wm.shape[0]-pd.merge(pb_wm, calypso_wm_grouped, on=['data_ref', 'book', 'ticker', 'currency'], how='left').shape[0]
        if check!=0:
            print ('%s linhas foram duplicadas durante o barimento de WM!!!! Verificar!' %check)
            
        return calypso_wm, calypso_wm_grouped

def ajuste_contas_calypso(df):
    # Faz o ajuste das contas do calypso, somando pelas variáveis abaixo e pegando somente as linhas negativas
    calypso = df[df.quantidade!=0].copy()
    calypso_ajuste = calypso.groupby(by=['conta_pb','data_ref', 'ticker','currency']).sum().reset_index()
    calypso_ajuste = calypso_ajuste[calypso_ajuste['quantidade']<0].copy()
    calypso_ajuste['acc'] = calypso_ajuste['conta_pb'].map(dict_contas)
    calypso_ajuste = calypso_ajuste.groupby(by=['acc','data_ref', 'ticker','currency']).sum().reset_index()
    calypso['acc'] = calypso['conta_pb'].map(dict_contas)

    # Aqui ainda faz parte do calypso_ajuste. Estou transferindo as informações entre as bases
    calypso = pd.merge(calypso, calypso_ajuste, on=['acc', 'data_ref', 'ticker', 'currency'], how='left')
    #Aqui eu estou tirando as linhas que não foram encontradas na volta. lembrar que o Calypso_teste derrubou um monte de linhas
    #todas aquelas que não tinham as informações que eram de aluguel doado.
    #Assim, teoricamente, todas as linhas desse novo calypso dizem respeito a posições tomadoras de aluguel.
    calypso = calypso[calypso['quantidade_y'].isnull()==False].copy().reset_index(drop=True)
    calypso = calypso.drop(['quantidade_y', 'year_y'], axis=1).rename(columns={
        'quantidade_x':'quantidade',
        'year_x':'year',
    })

    return calypso    


def puxa_ticker_client(x, pras_book, abertura_treas_ops):
    acc = abertura_treas_ops['account_client'][x]
    ticker = abertura_treas_ops['ticker'][x]
    date = abertura_treas_ops['date'][x]
    
    try:
        book = pras_book[(pras_book['Account Name']==acc)&(pras_book['PRODUCT_CODE.TICKER']==ticker)&\
                (pras_book['date']==date)]['Book'].reset_index(drop=True)[0]
    except IndexError:
        if acc=='2698':
            acc= 'BTG INT G BTG CAYMAN USD'
            try:
                book = pras_book[(pras_book['Account Name']==acc)&(pras_book['PRODUCT_CODE.TICKER']==ticker)&\
                            (pras_book['date']==date)]['Book'].reset_index(drop=True)[0]
            except IndexError:
                print ('%s -- %s -- %s' %(acc, ticker, date))
                book = np.nan
        else:
            print ('%s -- %s -- %s' %(acc, ticker, date))
            book = np.nan
    return book



def pega_data_file(file):
    lista_erros = []
    try:
        try:
            data = pd.to_datetime(file[-12:-4], format='%Y%m%d')
        except ValueError:
            try:
                data = pd.to_datetime(file[-14:-4], format='%Y-%m-%d')
            except ValueError:
                data = pd.to_datetime(file[-13:-5], format='%Y%m%d')    
    except ValueError:
        print ('    O arquivo %s não possui data registrada' %(file))
        data = 0
    return data    
    
    

def final_path(mes_ref, ano_ref, referencia, data):
    save_path = r'\\DRIOC0231PFS\Apoio_SB\Geral\BD\Aluguel_Offshore\Arquivos diários'
    if referencia == 'month':
        subfolder = mes_ref+str(ano_ref)
        final_path = save_path+'\\'+subfolder+'\\'+'consolidado'
        if os.path.isdir(save_path+'\\'+subfolder)==True:
            if os.path.isdir(save_path+'\\'+subfolder+'\\'+'consolidado')==False:
                os.mkdir(save_path+'\\'+subfolder+'\\'+'consolidado')
        else:
            os.mkdir(save_path+'\\'+subfolder)
            os.mkdir(save_path+'\\'+subfolder+'\\'+'consolidado')
        out_path = save_path+'\\'+subfolder+'\\'+'consolidado'
    else:
        subfolder = months_dict[pd.to_datetime(data).month]+str(pd.to_datetime(data).year)
        final_path = save_path+'\\'+subfolder+'\\'+data.strftime('%Y-%m-%d')
        if os.path.isdir(save_path+'\\'+subfolder)==True:
            if os.path.isdir(save_path+'\\'+subfolder+'\\'+data.strftime('%Y-%m-%d'))==False:
                os.mkdir(save_path+'\\'+subfolder+'\\'+data.strftime('%Y-%m-%d'))                
        else:
            os.mkdir(save_path+'\\'+subfolder)
            os.mkdir(save_path+'\\'+subfolder+'\\'+data.strftime('%Y-%m-%d'))
        out_path = save_path+'\\'+subfolder+'\\'+data.strftime('%Y-%m-%d')
        
    return out_path  
  

months_dict = {
    1:'jan',
    2:'fev',
    3:'mar',
    4:'abr',
    5:'mai',
    6:'jun',
    7:'jul',
    8:'ago',
    9:'set',
    10:'out',
    11:'nov',
    12:'dez'
}

dict_contas = {
    '038CDB895':'int_c',
    '038CDBD08':'ms_cayman',
    '038CDCN39':'ms_cayman',
    '038CDA715':'ms_cayman',
    '038CDCVS5':'ms_cayman',
    '038CDCSF7':'ms_cayman',
    '75201835':'ubs_cayman',
    '75202213':'ubs_cayman',
    '75202215':'ubs_cayman'
}    
    

    
    
'''    def ajustes(self, ubs, morgan, pras, bdwm, intc, ticker_diffs):        
        pb = get_pb(morgan, ubs)
        calypso = ajuste_calypso(pras, bdwm, intc)
        calypso_1 = calypso.copy()
        calypso_1['acc'] = calypso_1['conta_pb'].map(dict_contas)
        pb, calypso = ajuste_dias(pb, calypso)
        calypso = limpa_calypso(calypso)
        
        
        #Fórmula que também está definida no arquivo aluguel_offshore.py
        mapa_dict = mapeamento_tickers(pb, calypso)
        
        ticker_diffs = ticker_diffs.rename(columns={
            'Stock':'ticker',
            'Isin':'isin',
            'Cusip':'cusip'
        })

        mapa_dict_tickers = mapeamento_tickers(ticker_diffs, calypso)
        ticker_diffs['ticker'] = ticker_diffs['ticker'].map(mapa_dict_tickers)
        
        return pb, calypso, calypso_1, mapa_dict, ticker_diffs, mapa_dict_tickers
        
        
        
        
        
        
def ajuste_ubs(ubs):   
    ubs['date'] = pd.to_datetime(ubs['date'], format='%Y-%m-%d')
    ubs['date'] = np.where(ubs['date'].dt.weekday==6, ubs['date']-datetime.timedelta(2), ubs['date'])
    
    
    ubs['pb'] = 'ubs'
    ubs['month_number'] = ubs['date'].dt.month
    ubs['year'] = ubs['date'].dt.year
    ubs['month'] = ubs.date.dt.month.map(months_dict)
    
    ubs['cusip'] = np.nan
    ubs = ubs[['Reference Account Id' ,'pb', 'date', 'Ticker', 'ISIN', 'cusip', 'Quantity',
               'Daily Accrual', 'Billing CCY', 'month', 'year']].drop_duplicates().reset_index(drop=True)
    ubs.columns = ['conta', 'pb', 'data_ref', 'ticker', 'isin', 'cusip', 'qt', 'accrual', 'currency', 'month', 'year']
    ubs = ubs.drop_duplicates(subset=['conta', 'data_ref', 'ticker', 'qt', 'currency']).reset_index(drop=True)    
    return ubs

def ajuste_calypso(pras, bdwm, intc):
    pras['tipo'] = 'ASSET'
    bdwm['tipo'] = 'WM'
    intc['tipo'] = 'INT C'
    calypso = pd.concat([pras, bdwm, intc], axis=0).reset_index(drop=True)    
    calypso['date'] = pd.to_datetime(calypso['date'])
    calypso['month_number'] = calypso['date'].dt.month
    calypso['year'] = calypso['date'].dt.year
    calypso['month'] = calypso.date.dt.month.map(months_dict)

    calypso = calypso[['Account Name','tipo', 'Agent','date', 'shares', 'Book', 'PRODUCT_CODE.TICKER', 'PRODUCT_CODE.ISIN', 
                       'PRODUCT_CODE.CUSIP', 'Product Currency', 'month', 'year']].reset_index(drop=True)
    calypso.columns = ['conta_pb','conta', 'agent', 'data_ref', 'quantidade', 'book', 'ticker', 'isin', 'cusip',                        'currency', 'month', 'year']
    return calypso


def ajuste_morgan(morgan):
    morgan['date'] = pd.to_datetime(morgan['Value Date'], errors='coerce', format = '%m/%d/%Y')

    morgan['pb'] = 'ms'
    morgan['month_number'] = morgan['date'].dt.month
    morgan['year'] = morgan['date'].dt.year
    morgan['month'] = morgan.date.dt.month.map(months_dict)
    morgan = morgan[['Account', 'pb', 'date', 'Symbol', 'ISIN', 'Cusip', 'Shares', 'Net Borrow Cost', 'Currency', 'month', 'year']] 
    morgan.columns = ['conta', 'pb', 'data_ref', 'ticker', 'isin', 'cusip', 'qt', 'accrual', 'currency', 'month', 'year']  
    morgan['data_ref'] = np.where(morgan['data_ref'].dt.weekday==6, morgan['data_ref']-datetime.timedelta(2), morgan['data_ref'])
    morgan = morgan.drop_duplicates().reset_index(drop=True)    
    return morgan

def get_pb(morgan, ubs):
    ubs = ajuste_ubs(ubs)
    morgan = ajuste_morgan(morgan)    
    pb = pd.concat([morgan, ubs], axis=0).reset_index(drop=True)
    pb.qt = (pb.qt.replace( '[)]','', regex=True )
               .replace( '[(]','-',   regex=True ).astype(float))    
    pb.accrual = (pb.accrual.replace( '[)]','', regex=True )
               .replace( '[(]','-',   regex=True ).astype(float))
    
    pb['qt'] = -abs(pb['qt'])
    return pb



def mapeamento(mapa_dict, x):
    try:
        mapa_dict[x]
    except:
        mapa = np.nan
    else:
        mapa = mapa_dict[x]    
    return mapa



def mapeamento_tickers(pb, calypso):
    
    tickers_calypso = calypso[['ticker', 'isin', 'cusip']].drop_duplicates().copy()
    tickers_pb = pb[['ticker', 'isin', 'cusip']].drop_duplicates().copy()
    on_isin = pd.merge(tickers_pb[tickers_pb['isin'].isnull()==False], tickers_calypso, on='isin', how='left')\
                                                                                    .drop(['cusip_y'], axis=1)
    on_isin.columns = ['ticker_pb', 'isin', 'cusip', 'ticker_byisin'] 
    on_cusip = pd.merge(on_isin,  tickers_calypso[tickers_calypso['cusip'].isnull()==False], on=['cusip'], how = 'left')\
                                                                                        .drop('isin_y', axis=1).rename(columns={
        'ticker':'ticker_bycusip'
    })
    on_cusip['ticker_novos'] = np.where(on_cusip['ticker_byisin'].isnull()==False, on_cusip['ticker_byisin'],\
                                     on_cusip['ticker_bycusip'])
    on_cusip_1 = on_cusip[on_cusip['ticker_novos'].isnull()==False]
    on_cusip_2 = on_cusip[on_cusip['ticker_novos'].isnull()==True]
    on_cusip_2['ticker_novos'] = np.where(on_cusip_2['isin_x'].str[:2]=='US', on_cusip_2['ticker_pb']+' US', \
                                          on_cusip_2['ticker_novos'])
    on_cusip = pd.concat([on_cusip_1, on_cusip_2], axis=0)
    mapa_tickers = on_cusip[['ticker_pb','ticker_novos']]
    mapa_tickers = mapa_tickers[['ticker_pb', 'ticker_novos']].dropna().reset_index(drop=True).copy()
    mapa_dict = mapa_tickers.set_index('ticker_pb')['ticker_novos'].to_dict()
    
    return mapa_dict

def ajuste_dias(pb, calypso):
    #Pega somente os arquivos do calypso que se referem às contas da asset
    calypso.conta_pb = calypso.conta_pb.astype(str)
    calypso = calypso[calypso.conta_pb.isin(dict_contas.keys())].copy()
    #Retira sábados e domingos da base
    pb = pb[pb.data_ref.dt.weekday<5].copy()
    calypso = calypso[calypso.data_ref.dt.weekday<5].copy()
    #Como estamos pegando somente os dias úteis, multiplica o valor de sexta por 3 para levar em consideração dias corridos
    pb['accrual_adjusted'] = np.where(pb.data_ref.dt.weekday==4, pb['accrual']*3, pb['accrual'])
    pb['conta'] = pb['conta'].astype(str)
    #Aplica o dicionário de contas que também está no aluguel_offshore.py
    pb['acc'] = pb['conta'].apply(lambda x: dict_contas[x])
    
    return pb, calypso

def limpa_calypso(calypso):
    #Tem que fazer por currency também por causa da ordem de grandeza de algumas delas. pode ser que fiquemos expostos se não colocar
    calypso_ajuste = calypso.groupby(by=['conta_pb','data_ref', 'ticker','currency']).sum().reset_index()
    calypso_ajuste = calypso_ajuste[calypso_ajuste['quantidade']<=0].copy()
    calypso_ajuste['acc'] = calypso_ajuste['conta_pb'].map(dict_contas)
    calypso_ajuste = calypso_ajuste.groupby(by=['acc','data_ref', 'ticker','currency']).sum().reset_index()
    calypso_ajuste = calypso_ajuste[calypso_ajuste['quantidade']<0].copy()
    calypso['acc'] = calypso['conta_pb'].map(dict_contas)
    calypso = pd.merge(calypso, calypso_ajuste, on=['acc', 'data_ref', 'ticker', 'currency'], how='left')
    
    
    #Aqui eu estou tirando as linhas que não foram encontradas na volta. lembrar que o Calypso_teste derrubou um monte de linhas
    #todas aquelas que não tinham as informações que eram de aluguel doado.
    #Assim, teoricamente, todas as linhas desse novo calypso dizem respeito a posições tomadoras de aluguel.
    calypso = calypso[calypso['quantidade_y'].isnull()==False].copy().reset_index(drop=True)

    calypso = calypso.drop(['quantidade_y', 'year_y'], axis=1).rename(columns={
        'quantidade_x':'quantidade',
        'year_x':'year',
    })
    
    return calypso



def ajuste_wm(bdwm, data, mes_ref, ano_ref, referencia = 'month'):
    
    calypso_wm = bdwm.copy()

    calypso_wm['tipo'] = 'WM' 
    calypso_wm['date'] = pd.to_datetime(calypso_wm['date'])
    calypso_wm['month_number'] = calypso_wm['date'].dt.month
    calypso_wm['year'] = calypso_wm['date'].dt.year
    calypso_wm['month'] = calypso_wm.date.dt.month.map(months_dict)
    calypso_wm = calypso_wm[['Account Name','tipo', 'Agent','date', 'shares', 'Book', 'PRODUCT_CODE.TICKER', 'PRODUCT_CODE.ISIN', 
                       'PRODUCT_CODE.CUSIP', 'Product Currency', 'month', 'year', 'LE Name']].reset_index(drop=True)
    calypso_wm.columns = ['conta_pb','conta', 'agent', 'data_ref', 'quantidade', 'book', 'ticker', 'isin', 'cusip', 
                  'currency', 'month', 'year', 'cliente']
    
    if referencia=='month':
        calypso_wm = calypso_wm[(calypso_wm['month']==mes_ref)&(calypso_wm['data_ref'].dt.year==ano_ref)]
        calypso_wm_acumulado = np.nan
        
    else:
        calypso_wm_acumulado = calypso_wm[(calypso_wm['data_ref'].dt.month==pd.to_datetime(data).month)&\
                                         (calypso_wm['data_ref'].dt.year==pd.to_datetime(data).year)&\
                                         (calypso_wm['data_ref']<=pd.to_datetime(data))]
        calypso_wm = calypso_wm[calypso_wm['data_ref']==pd.to_datetime(data)]
        
    calypso_wm['quantidade'] = -1*calypso_wm['quantidade']
    calypso_wm = calypso_wm[calypso_wm['quantidade']<0]
    calypso_wm_grouped =calypso_wm.groupby(by=['data_ref', 'book', 'ticker', 'currency']).sum().reset_index()
      
    try:
        calypso_wm_acumulado['quantidade'] = -1*calypso_wm_acumulado['quantidade']
        calypso_wm_acumulado = calypso_wm_acumulado[calypso_wm_acumulado['quantidade']<0]
        calypso_wm_grouped_acumulado =calypso_wm_acumulado.groupby(by=['data_ref', 'book', 'ticker', 'currency']).sum().reset_index()
    except:
        calypso_wm_acumulado = np.nan
        calypso_wm_grouped_acumulado = np.nan
        print ('Sem valores de acumulado')
    return calypso_wm, calypso_wm_grouped, calypso_wm_acumulado, calypso_wm_grouped_acumulado

def get_batimento_wm_distb(batimento_wm, calypso_wm, abertura_batidos):
    
    batimento_wm_batidos = batimento_wm[batimento_wm['quantidade_book']==batimento_wm['quantidade']].copy()
    batimento_wm_batidos['id'] = range(1, batimento_wm_batidos.shape[0] +1)
    batimento_wm_batidos['status'] = 'batido'
    batimento_wm_divergentes = batimento_wm[batimento_wm['quantidade_book']!=batimento_wm['quantidade']].copy()
    batimento_wm_divergentes['status'] = 'divergente'
    batimento_wm_sobra_destino = batimento_wm[batimento_wm['quantidade'].isnull()==True]
    batimento_wm_sobra_destino['status'] = 'n batido'
    batimento_wm_distrib = pd.merge(calypso_wm, batimento_wm_batidos, on=['data_ref', 'book', 'ticker', 'currency'], how='left')\
    [['conta_pb_x', 'agent_x', 'data_ref', 'quantidade_x', 'book', 'ticker', 'currency', 'cliente','quantidade_book', 
      'acc', 'status','accrual_final', 'id']].rename(columns={
        'quantidade_book':'quantidade_ticker',
        'quantidade_x':'quantidade_book',
        'conta_pb_x':'conta_pb',
        'agent_x':'agent',
        'cliente':'conta'   
    })
    batimento_wm_sobra_origem = batimento_wm_batidos[~batimento_wm_distrib['id'].isin(batimento_wm_batidos['id'].drop_duplicates())]
    batimento_wm_distrib = batimento_wm_distrib.drop('id', axis=1)
    n_batimento_wm_distrib = batimento_wm_distrib[batimento_wm_distrib['quantidade_ticker'].isnull()==True]\
    .drop(['quantidade_ticker'], axis=1)
    batimento_wm_distrib = batimento_wm_distrib[batimento_wm_distrib['quantidade_ticker'].isnull()==False]
    batimento_wm_distrib['pct'] = batimento_wm_distrib['quantidade_book']/batimento_wm_distrib['quantidade_ticker']
    batimento_wm_distrib['accrual'] = batimento_wm_distrib['accrual_final']*batimento_wm_distrib['pct']
    batimento_wm_distrib = batimento_wm_distrib.drop(['quantidade_ticker', 'pct'], axis=1).rename(columns = {
    'accrual_final':'accrual_n_distrib','accrual':'accrual_final'})

    
    #abertura_batidos['conta_pb'] = abertura_batidos['acc'].copy()
    
    #n_distrib_wm = abertura_batidos[((abertura_batidos['book'].str.contains('PRIVATE'))|\
    #                   (abertura_batidos['book'].str.contains('CLIENT')))]
    #abertura_batidos = abertura_batidos[~((abertura_batidos['book'].str.contains('PRIVATE'))|\
    #                   (abertura_batidos['book'].str.contains('CLIENT')))] 
    #abertura_batidos_final = pd.concat([abertura_batidos, batimento_wm_distrib], axis=0)
    
    
    return batimento_wm_distrib, abertura_batidos_final, n_batimento_wm_distrib, n_distrib_wm, batimento_wm_sobra_origem


def get_month_or_day_batimento(calypso, pb,mes_ref, ano_ref, data, referencia = 'month'):
    if referencia=='month':
        calypso_month = calypso[(calypso.month==mes_ref)&(calypso.year==ano_ref)]\
                    .drop(['book', 'isin', 'cusip', 'month', 'year'], axis=1).reset_index(drop=True).copy()
        pb_month = pb[(pb.month==mes_ref)&(pb.year==ano_ref)]\
                    .drop(['ticker_antigo', 'isin', 'cusip', 'accrual', 'month', 'year'], axis=1).reset_index(drop=True).copy()
        calypso_month_acumulado = np.nan
        pb_month_acumulado = np.nan
        batimento_string = 'Você está fazendo o batimento referente a %s/%s' %(mes_ref, ano_ref)
    else:
        calypso_month = calypso[calypso.data_ref==pd.to_datetime(data)]\
                    .drop(['book', 'isin', 'cusip', 'month', 'year'], axis=1).reset_index(drop=True).copy()
        calypso_month_acumulado =  calypso[(calypso.data_ref.dt.month==pd.to_datetime(data).month)&(calypso.data_ref.dt.year==pd.to_datetime(data).year)&(calypso.data_ref<=pd.to_datetime(data))]\
                    .drop(['book', 'isin', 'cusip', 'month', 'year'], axis=1).reset_index(drop=True).copy()
        pb_month = pb[pb.data_ref==pd.to_datetime(data)]\
                    .drop(['ticker_antigo', 'isin', 'cusip', 'accrual', 'month', 'year'], axis=1).reset_index(drop=True).copy()
        pb_month_acumulado =  pb[(pb.data_ref.dt.month==pd.to_datetime(data).month)&(pb.data_ref.dt.year==pd.to_datetime(data).year)&(pb.data_ref<=pd.to_datetime(data))]\
            .drop(['ticker_antigo', 'isin', 'cusip', 'accrual', 'month', 'year'], axis=1).reset_index(drop=True).copy()
            
        batimento_string = 'Você está fazendo o batimento referente ao dia %s' %(data)
    
    print(batimento_string)
    return calypso_month, pb_month, calypso_month_acumulado, pb_month_acumulado


def ajustes_pb_calypso_month(pb_month, calypso_month, dict_contas):
    
    #Agrupa as informações que estão no calypso eliminando books. Junta em conta_pb, agent, data_ref, ticker e currency
    calypso_batimento = calypso_month.groupby(by=['conta_pb','agent','data_ref','ticker','currency']).sum().copy().reset_index()
    calypso_batimento['acc'] = calypso_batimento['conta_pb'].map(dict_contas)
    calypso_batimento = calypso_batimento[calypso_batimento['quantidade']<0].reset_index(drop=True)
    calypso_batimento = calypso_batimento.groupby(by=['acc','data_ref', 'ticker','currency']).sum().reset_index()
    calypso_batimento = calypso_batimento[calypso_batimento['quantidade']<0].reset_index(drop=True)   
    #é somente um indice para poder checar quais informações do calypso não passaram pelo filtro da PB
    calypso_batimento['id'] = range(1, calypso_batimento.shape[0] +1)
    
    pb_month = pb_month.groupby(by=['acc','data_ref','ticker','currency']).sum().reset_index()
    
    return pb_month, calypso_batimento

def batimento_calypso_pb(pb_month, calypso_batimento, ticker_diffs):
    
    calypso_bate_pb = pd.merge(pb_month, calypso_batimento, on=['acc','data_ref','ticker','currency'],  how='left')
    sobra_destino = calypso_bate_pb[(calypso_bate_pb['quantidade'].isnull()==True)&(calypso_bate_pb['accrual_adjusted']!=0)]
    calypso_bate_pb = calypso_bate_pb[calypso_bate_pb['quantidade'].isnull()==False]
    
    
    pct_in_calypso_not_in_pb=calypso_batimento[~calypso_batimento['id'].isin(calypso_bate_pb['id'].dropna().drop_duplicates())].shape[0]/\
                                    calypso_batimento.shape[0]*100    
    
    
    sobra_origem = calypso_batimento[~calypso_batimento['id'].isin(calypso_bate_pb['id'].dropna().drop_duplicates())]
    batido = calypso_bate_pb[(calypso_bate_pb['quantidade'].isnull()==False)&\
                         (abs(calypso_bate_pb['qt'])==abs(calypso_bate_pb['quantidade']))].copy()
    batido['status']='batido'
    divergentes = calypso_bate_pb[(calypso_bate_pb['quantidade'].isnull()==False)&\
                         (abs(calypso_bate_pb['qt'])!=abs(calypso_bate_pb['quantidade']))].copy()
    
    corrigidos = divergentes[((divergentes['ticker'].isin(ticker_diffs['ticker']))&(divergentes['acc']!='ubs_cayman'))].copy()
    corrigidos['status'] = 'corrigido'
    
    n_batidos = divergentes[~((divergentes['ticker'].isin(ticker_diffs['ticker']))&(divergentes['acc']!='ubs_cayman'))].copy()
    n_batidos['status']='n_batido'
    distribuidos = pd.concat([batido, corrigidos, n_batidos], axis=0)
    
    conta_1 = (1-calypso_bate_pb.shape[0]/pb_month.shape[0])*100
    texto_1 = '%s pct dos trades estão no prime broker, mas não acharam correspondência no Calypso' % conta_1
    texto_2 = '%s pct dos trades foram achados no calypso, mas não têm correspondência no prime broker' % pct_in_calypso_not_in_pb
    
    print (texto_1)
    print(texto_2)
    
    return sobra_destino, sobra_origem, batido, divergentes, corrigidos, n_batidos, distribuidos


def get_calypso_month_books(calypso,mes_ref, ano_ref, data, referencia = 'month'):
    
    if referencia == 'month':
        calypso_month_books = calypso[(calypso.month==mes_ref)&(calypso.year==ano_ref)].copy()
        calypso_month_books_acumulado = np.nan
        batimento_string = 'Você está fazendo a distribuição referente a %s/%s' %(mes_ref, ano_ref)
        
    else:
        calypso_month_books = calypso[calypso.data_ref==pd.to_datetime(data)].copy()
        calypso_month_books_acumulado = calypso[(calypso.data_ref.dt.month==pd.to_datetime(data).month)&\
                                               (calypso.data_ref.dt.year==pd.to_datetime(data).year)&\
                                               (calypso.data_ref<=pd.to_datetime(data))].copy()
        batimento_string = 'Você está fazendo a distribuição referente ao dia %s' %(data)
    
    print(batimento_string)
    return calypso_month_books, calypso_month_books_acumulado  


def get_name(mes_ref, ano_ref, data, referencia = 'month'):
    if referencia == 'month':
        string = mes_ref+'-'+str(ano_ref)
    else:
        string =  str(data)
        
    return string


def check_days(calypso_month, pb_month):

    dias_calypso = calypso_month[['acc', 'data_ref']].copy()
    dias_calypso['tipo'] = 'calypso'
    dias_pb = pb_month[['acc', 'data_ref']].copy()
    dias_pb['tipo'] = 'pb'
    dias_ok = pd.concat([dias_calypso, dias_pb], axis=0)
    dias_ok['check'] = 1
    pvt = pd.pivot_table(dias_ok, values=['check'],
                         index='data_ref', columns=['tipo','acc'])
    
    return pvt

def explode_books(calypso_month_books, calypso_batimento, distribuidos):
    calypso_month_books = pd.merge(calypso_month_books, calypso_batimento.drop('id', axis=1), \
                                   on=['acc','data_ref','ticker','currency'], how='left').rename(columns={
        'quantidade_x':'quantidade_book',
        'quantidade_y':'quantidade_ticker'
    })

    calypso_month_books = calypso_month_books[calypso_month_books['quantidade_ticker'].isnull()==False]
    calypso_month_books = pd.merge(calypso_month_books, distribuidos, on=['acc','data_ref','ticker','currency'], how='left')
    calypso_month_books = calypso_month_books[calypso_month_books['quantidade_book']!=0]
    print ('Ajustes na base calypso estão completos')
    
    por_book = calypso_month_books.groupby(by=['conta_pb','data_ref','ticker','currency']).sum().reset_index()
    calypso_month_books = pd.merge(calypso_month_books, por_book.drop(['year', 'qt', 'accrual_adjusted',\
                                                                       'quantidade', 'id', 'quantidade_ticker'], axis=1), \
                                                           on=['conta_pb','data_ref','ticker','currency'], how='left')\
    .rename(columns={
        'quantidade_book_x':'quantidade_book',
        'quantidade_book_y':'quantidade_conta_pb'
    })
    calypso_month_books = calypso_month_books[calypso_month_books['quantidade_conta_pb']<0]
    calypso_month_books = calypso_month_books[calypso_month_books['accrual_adjusted'].isnull()==False]
    print ('Ajustes de quantidades estão completos')
    
    abertura = calypso_month_books[calypso_month_books['id'].isin(distribuidos['id'].drop_duplicates())==True]
    abertura_n_batidos = calypso_month_books[calypso_month_books['id'].isin(distribuidos['id'].drop_duplicates())==False]
    print ('Checando quais trades ficaram fora do batimento')
    
    
    
    return calypso_month_books, abertura, abertura_n_batidos

def ajuste_abertura_checs(abertura, abertura_n_batidos, pb_month):
    
    abertura = abertura.drop(['isin', 'cusip','month', 'year', 'quantidade', 'id'], axis=1)
    abertura['percent'] = -(abertura['quantidade_book']/abertura['quantidade_ticker'])
    abertura['accrual_final'] = abertura['percent']*-1*abertura['accrual_adjusted']
    print ('Ajustes nas quantidades e alocação percentual feitos')
    abertura = abertura.drop(['conta_pb', 'quantidade_ticker', 'qt', 'accrual_adjusted',
                                          'quantidade_conta_pb', 'percent'], axis=1).reset_index(drop=True)
    abertura_batidos = abertura[abertura['status']!='n_batido']
    abertura_n_batidos = abertura[abertura['status']=='n_batido']
    print ('Ajustes nas bases feitos')
    
    bate_soma = abertura.groupby(by=['acc', 'currency']).sum().reset_index()
    bate_soma_pb = pb_month.groupby(by=['acc', 'currency']).sum().reset_index()
    print ('Geradas os dataframes de batimento')
    
    check = pd.merge(bate_soma_pb, bate_soma, on=['acc', 'currency'], how='left').rename(columns={
    'qt':'quantidade_pb',
    'accrual_adjusted':'custos_pb',
    'quantidade_book':'quantidade_calypso',
    'accrual_final':'custos_batidos'
})
    check['bate_qt'] = check['quantidade_pb']-check['quantidade_calypso']
    check['bate_custos'] = check['custos_pb']-check['custos_batidos']
    check['bate_custos_pct'] = check['custos_pb']/check['custos_batidos']
    check = check[['acc', 'currency', 'quantidade_pb', 'quantidade_calypso', 'bate_qt', 'custos_pb', 'custos_batidos',
          'bate_custos', 'bate_custos_pct']]   
    print ('Dataframe de batimento gerado')
    
    return abertura, abertura_batidos, abertura_n_batidos, bate_soma, bate_soma_pb, check'''
    
