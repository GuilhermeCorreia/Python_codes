
# coding: utf-8

# In[ ]:

import os
import sys
sys.path.append('%s/../' % os.getcwd())

import datetime
import pandas as pd
import numpy as np
import getpass


# In[ ]:

def info_base_pb_to_get_ticker(pb, x):
    ticker = str(pb[pb.index==x]['ticker'][x]).replace('/', '')
    isin = str(pb[pb.index==x]['isin'][x])
    cusip = str(pb[pb.index==x]['cusip'][x])
    sedol = str(pb[pb.index==x]['sedol'][x])
    return ticker, isin, cusip, sedol


# In[ ]:

def get_ticker_bases(calypso, pb, x):
    try:
        ticker_pb, isin, cusip, sedol = info_base_pb_to_get_ticker(pb, x)
        try:
            ticker = calypso[calypso['isin']==isin].drop_duplicates(subset=['ticker']).reset_index(drop=True)['ticker'][0]
            construct = 'isin'
        except IndexError:
            try:
                ticker = calypso[calypso['cusip']==cusip].drop_duplicates(subset=['ticker']).reset_index(drop=True)['ticker'][0]
                construct = 'cusip'
            except IndexError:
                ticker = calypso[calypso['sedol']==sedol].drop_duplicates(subset=['ticker']).reset_index(drop=True)['ticker'][0]
                construct = 'sedol'
        return [ticker, construct]
    except IndexError:
        ticker_pb, isin, cusip, sedol = info_base_pb_to_get_ticker(pb, x)
        print('O ticker %s não foi encontrado pelos códigos.\n Tentaremos agora pelo nome' %(ticker_pb))
        try:
            ticker = ticker_pb.split('.')[0]
            ticker = calypso[calypso.ticker.str.contains(ticker_pb)].drop_duplicates(subset=['ticker'])\
                                                            .reset_index(drop=True)['ticker'][0]
            construct = 'nome'
            print('O ticker %s não foi encontrado pelo nome.\n Ele será então contruído pelo Ticker + Isin' %(ticker_pb))
        except IndexError:
            ticker = ticker.split('.')[0]
            ticker = str(ticker_pb)+' '+str(isin)[:2]
            construct = 'construido_ticker'
            print ('''Nós aconselhamos que você confira o ticker %s, porque ele foi ajustado pelo Isin.
Caso ele esteja ERRADO você deverá fazer o ajuste na próxima parte.''' %(ticker_pb))
        except ValueError:
            ticker = ticker_pb + ' US'
            construct = 'ticker+US'
        return [ticker, construct]
    except ValueError:
        print(r'O ticker %s não foi encontrado em nenhuma instância.\n Proceder com inserção manual' %(ticker_pb))
        return [np.nan, np.nan]
