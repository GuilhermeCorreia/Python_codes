
# coding: utf-8

# In[12]:

from bs4 import BeautifulSoup
# In[13]:
class PortfolioImporter(object):

    def __init__(self, xml):
        self.xml = BeautifulSoup(open(xml, 'r').read(), 'lxml')
        self.headers = []
        self.cotas = []
        
    def parse(self):
        self.get_header()
        self.get_cotas()
        
    def get_header(self):
        childrens = self.xml.fundo.find_all('header')
                
        for c in childrens:
            self.headers.append({
                'isin': c.isin.text,
                'cnpj': c.cnpj.text,
                'nome': c.nome.text,
                'dtposicao': c.dtposicao.text,
                'nomeadm': c.nomeadm.text,
                'cnpjadm': c.cnpjadm.text,
                'nomegestor': c.nomegestor.text,
                'cnpjgestor': c.cnpjgestor.text,
                'nomecustodiante': c.nomecustodiante.text,
                'cnpjcustodiante': c.cnpjcustodiante.text,
                'valorcota': c.valorcota.text,
                'quantidade': c.quantidade.text,
                'patliq': c.patliq.text,
                'valorativos': c.valorativos.text,
                'valorreceber': c.valorreceber.text,
                'valorpagar': c.valorpagar.text,
                'vlcotasemitir': c.vlcotasemitir.text,
                'vlcotasresgatar': c.vlcotasresgatar.text,
                'codanbid': c.codanbid.text,
                'tipofundo': c.tipofundo.text,
                'nivelrsc': c.nivelrsc.text,
            })
            
    def get_cotas(self):
        childrens = self.xml.fundo.find_all('header')
        
        for c in childrens:
            dtposicao = c.dtposicao.text
            cnpj_rb = c.cnpj.text
        
        childrens = self.xml.fundo.find_all('cotas') #retorna uma lista 
        for c in childrens:
            self.cotas.append({
                'dtposicao': dtposicao,
                'cnpj_rb': cnpj_rb,
                'fisin': c.isin.text,
                'fcnpj': c.cnpjfundo.text,
                'fqtcota': c.qtdisponivel.text,
                'fcota': c.puposicao.text,
            })
        childrens = self.xml.fundo.find_all('titpublico')
        for c in childrens:
            self.cotas.append({
                'dtposicao': dtposicao,
                'cnpj_rb': cnpj_rb,
                'tisin':c.isin.text,
                'tdtemissao': c.dtemissao.text,
                'tdtoperacao': c.dtoperacao.text,
                'tdtvencimento':c.dtvencimento.text,
                'tqtdisponivel':c.qtdisponivel.text,
                'tpucompra':c.pucompra.text,
                'tpuposicao':c.puposicao.text,
                'tpuemissao':c.puemissao.text,
                'tprincipal':c.principal.text,
                'tcoupom':c.coupom.text,
                
            })