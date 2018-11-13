
# coding: utf-8

import os
import sys
sys.path.append('%s/../' % os.getcwd())

import datetime
import pandas as pd
import numpy as np
import getpass

def pega_data_file(file):
    '''Essa função testa se um arquivo está dentro do range de datas escolhido (obs: os nomes dos arquivos devem estar dentro do padrão)'''
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

class TratamentoDosDados(object):
    '''Classe destinada a tratar os dados vindos das planilhas insumo (calypso e PB)'''
    def __init__(self,pasta,data_inicio,data_final):
        self.pasta= pasta
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.lista_files = self.povoa_lista_files()
        self.ubs, self.morgan, self.intc, self.bdwm, self.pras = self.baixa_dados_df()
        self.pb, self.calypso, self.calypso_1 = self.tabelas_ajustadas()
        
        
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
        print('Baixando arquivos!!')
        
        lista_files = self.lista_files
        pasta = self.pasta
        ubs_count=0
        morgan_count=0
        pras_count=0
        bdwm_count=0
        intc_count=0     
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
    
    def baixa_tabelas_raw(self):
        
        ubs = self.ubs
        morgan = self.morgan
        intc = self.intc
        bdwm = self.bdwm
        pras = self.pras
        
        return ubs, morgan, intc, bdwm, pras
    
    def ajusta_tabelas_ubs(self):
        ubs = self.ubs
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
    def ajusta_tabelas_morgan(self):
        morgan = self.morgan
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
    
    def ajusta_tabelas_pb(self):
        ubs = self.ajusta_tabelas_ubs()
        morgan = self.ajusta_tabelas_morgan()
        pb = pd.concat([morgan, ubs], axis=0).reset_index(drop=True)
        pb.qt = (pb.qt.replace( '[)]','', regex=True )
                   .replace( '[(]','-',   regex=True ).astype(float))    
        pb.accrual = (pb.accrual.replace( '[)]','', regex=True )
                   .replace( '[(]','-',   regex=True ).astype(float))
        pb['qt'] = -abs(pb['qt'])
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
    
    def ajusta_tabelas_calypso(self):
        pras = self.pras
        bdwm = self.bdwm
        intc = self.intc
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
    def tabelas_ajustadas(self):
        pb = self.ajusta_tabelas_pb()
        calypso, calypso_1 = self.ajusta_tabelas_calypso()
        
        return pb, calypso, calypso_1

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