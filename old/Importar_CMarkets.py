import win32com.client
import pandas as pd
import numpy as np
import os
import urllib2 
import datetime
import requests    
    
class ImportCMarkets(object):
    
    def __init__(self,messages,data):
        self.messages=messages
        self.data=data
        self.dia()

    def dia(self):
        data = self.data
        messages=self.messages
        string_1 = 'ENC: CALL'
        string_2='ENC: FE'
        for msg in messages:
            try:
                msg.senton
            except:
                continue
            else:
                data_ref = pd.to_datetime(str(msg.senton).split()[0], format='%m/%d/%y')
            if data_ref==data:
                if string_1 in msg.Subject:
                    if 'ENC: CALL PAP' in msg.Subject:
                        try:
                            msg.Attachments(1)
                        except:
                            continue
                        else:
                            att= msg.Attachments(1)
                            att.SaveAsFile(os.getcwd() + '\\new.xlsm')

                            a=0
                            for i in range(0,50):
                                head = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,skiprows=i))
                                try:
                                    head['Vencimento']
                                except:
                                    continue
                                else:
                                    if a !=0:
                                        b=i
                                        break
                                    else:
                                        a=i
                            try:
                                df_ltn
                            except:
                                dn = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,header=a,parse_cols="C:I"))
                                df_ltn=dn.iloc[:(b-a-1),:].copy()
                                df_ltn['data']=msg.senton
                                df_ntnf=dn.iloc[(b-a):,:].copy()
                                df_ntnf['data']=msg.senton
                            else:
                                dn = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,header=a,parse_cols="C:I"))
                                df_ltn_n=dn.iloc[:(b-a-1),:].copy()
                                df_ltn_n['data']=msg.senton
                                df_ntnf_n=dn.iloc[(b-a):,:].copy()
                                df_ntnf_n['data']=msg.senton
                                frames1=[df_ltn,df_ltn_n]
                                frames2=[df_ntnf,df_ntnf_n]
                                df_ltn=pd.concat(frames1)
                                df_ntnf=pd.concat(frames2)
                    elif 'ENC: CALL NTN-B' in msg.Subject:
                        try:
                            msg.Attachments(1)
                        except:
                            continue
                        else:
                            att= msg.Attachments(1)
                            att.SaveAsFile(os.getcwd() + '\\new.xlsm')
                            a=0
                            for i in range(0,50):
                                head = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,skiprows=i))            
                                try:
                                    head['Vencimento']
                                except:
                                    continue
                                else:
                                    a=i
                                    break
                            try:
                                df_ntnb
                            except:
                                df_ntnb = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,header=a,parse_cols="C:H"))
                                df_ntnb['data']=msg.senton
                            else:
                                df_ntnb_n = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,header=a,parse_cols="C:H"))
                                df_ntnb_n['data']=msg.senton
                                frames=[df_ntnb,df_ntnb_n]
                                df_ntnb=pd.concat(frames)



                elif string_2 in msg.Subject:
                    try:
                        msg.Attachments(1)
                    except:
                        continue
                    else:
                        att= msg.Attachments(1)
                        att.SaveAsFile(os.getcwd() + '\\new.xlsm')

                        a=0
                        for i in range(0,150):
                            head = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,skiprows=i))
                            try:
                                head['Vencimento']
                            except:
                                continue
                            else:
                                a=i
                                break
                        try:
                            df_fch
                        except:
                            df_fch=pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,header=a,parse_cols="E:K"))
                            df_fch['data']=msg.senton
                        else:    
                            dn_fch = pd.DataFrame(pd.read_excel(os.getcwd() + '\\new.xlsm',sheetname=0,header=a,parse_cols="E:K"))
                            dn_fch['data']=msg.senton
                            frames=[dn_fch,df_fch]
                            df_fch=pd.concat(frames)
                        
        try:
            df_ltn
        except:
            df_ltn = 0
            df_ntnf=0
            df=0
        else:           
            df_ltn['titulo']='LTN'
            df_ntnf['titulo']='NTN-F'
            df_ntnf['Vencimento']=pd.to_datetime('20'+df_ntnf['Vencimento'].str.split(expand=True)[1]+'/01/01')
            df_ltn=df_ltn.replace(r'\s+', np.nan, regex=True).fillna(0)
            df_ntnf=df_ntnf.replace(r'\s+', np.nan, regex=True).fillna(0)
            try:
                df_ntnb
            except:
                frames=[df_ltn,df_ntnf]
            else:
                df_ntnb['titulo']='NTN-B'
                df_ntnb['Pts S/DI']=0.0
                df_ntnb=df_ntnb.replace(r'\s+', np.nan, regex=True).fillna(0)
                frames = [df_ltn,df_ntnf,df_ntnb]
            df = pd.concat(frames)

            df.rename(columns={
                                    'Vencimento':'vencimento',
                                    'Andima':'andima',
                                    'Pts S/DI':'pts_di',
                                    'Compra':'compra',
                                    'Venda':'venda',
                                    'Ult':'ultima',
                                    'Qtd':'quantidade'
                                    }, inplace=True)
            df[['andima','compra','pts_di','venda','ultima','quantidade']]=df[['andima','compra','pts_di','venda',
                                                                               'ultima','quantidade']].apply(pd.to_numeric,errors='coerce')
            df=df[df['andima']!=0.0]
            df=df.replace(r'\s+', np.nan, regex=True).dropna()
            df['vencimento']=pd.to_datetime(df['vencimento'])
            df['data']=pd.to_datetime(df['data'], format='%m/%d/%y %H:%M:%S')
            df['periodo']=np.where(df['data'].dt.hour<12.0,'manha','tarde')
            df=df.sort_values(by=['data','titulo','vencimento','periodo']).reset_index(drop=True)

        try:
            df_fch
        except:
            df_fch = 0
        else:
            df_fch=df_fch.dropna(subset=['Papel','Vencimento'])
            df_fch=df_fch[df_fch['Papel']!='Papel'].reset_index(drop=True).replace(r'\s+', np.nan, regex=True).fillna(0)
            df_fch['periodo']='fechamento'
            df_fch=df_fch.rename(columns={
                'Papel':'titulo',
                'Vencimento':'vencimento',
                'Taxa Compra':'taxa_compra_diferencial',
                'Taxa Venda':'taxa_venda_diferencial',
                df_fch.columns[4]:'ultimo_diferencial',
                'Estimativa':'estimativa_compra',
                'Unnamed: 6':'estimativa_venda'
            })
            df_fch['vencimento']=pd.to_datetime(df_fch['vencimento'])
            df_fch['data']=pd.to_datetime(df_fch['data'], format='%m/%d/%y %H:%M:%S')
            df_fch[['taxa_compra_diferencial','taxa_venda_diferencial','ultimo_diferencial','estimativa_compra',
                'estimativa_venda']]=df_fch[['taxa_compra_diferencial','taxa_venda_diferencial','ultimo_diferencial','estimativa_compra',
                'estimativa_venda']].apply(pd.to_numeric,errors='coerce')
        
        return df, df_fch
    
    
    
    
    
    
class ImportAnbima(object):
    import urllib2
    import pandas as pd
    import numpy as np
    import datetime
    import requests
    
    def __init__(self, data):
        self.data=data
        self.dados_anbima()
    
    
    
    def dados_anbima(self):
        data=self.data
        
        data_a=format_data(data)
        url = 'http://www.anbima.com.br/merc_sec/arqs/m'+str(data_a)+'.xls'
        print url

        
        downloaded_data = urllib2.urlopen(url)
        df_ltn = pd.read_excel(downloaded_data, header=3, sheetname='LTN')
        downloaded_data = urllib2.urlopen(url)
        df_ntnc = pd.read_excel(downloaded_data, header=3, sheetname='NTN-C')
        downloaded_data = urllib2.urlopen(url)
        df_lft = pd.read_excel(downloaded_data, header=3, sheetname='LFT')
        downloaded_data = urllib2.urlopen(url)
        df_ntnb = pd.read_excel(downloaded_data, header=3, sheetname='NTN-B')
        downloaded_data = urllib2.urlopen(url)
        df_ntnf = pd.read_excel(downloaded_data, header=3, sheetname='NTN-F')
        
        
        df_ltn=df_ltn.dropna()
        df_ltn['titulo']='LTN'
        df_ntnc=df_ntnc.dropna()
        df_ntnc['titulo']='NTN-C'
        df_lft=df_lft.dropna()
        df_lft['titulo']='LFT'
        df_ntnb=df_ntnb.dropna()
        df_ntnb['titulo']='NTN-B'
        df_ntnf=df_ntnf.dropna()
        df_ntnf['titulo']='NTN-F'
        frames = [df_ltn,df_ntnc,df_lft,df_ntnb,df_ntnf]
        df = pd.concat(frames)
        
        dic={
            df.columns[0]:'codigo_selic',
            df.columns[1]:'emissao',
            df.columns[2]:'vencimento',
            df.columns[3]:'compra',
            df.columns[4]:'venda',
            df.columns[5]:'tx_indicativa',
            df.columns[6]:'pu',
            df.columns[7]:'intervalo_indicativo_minimo_d0',
            df.columns[8]:'intervalo_indicativo_maximo_d0',
            df.columns[9]:'intervalo_indicativo_minimo_d1',
            df.columns[10]:'intervalo_indicativo_maximo_d1'
        }
        df=df.rename(columns=dic)
        df['periodo']='anbima'
        df['data']=data
        
        return df
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def format_data(data):
    dt_dic={
    '1':'jan',
    '2':'fev',
    '3':'mar',
    '4':'abr',
    '5':'mai',
    '6':'jun',
    '7':'jul',
    '8':'ago',
    '9':'set',
    '10':'out',
    '11':'nov',
    '12':'dez'
}
    return format(data, '%y'+dt_dic.get(str(data.month))+'%d')
        