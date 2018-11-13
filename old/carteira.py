# coding=utf-8

import datetime
from bs4 import BeautifulSoup


def str_to_float(sstr):
    """
    Função que converte string em float.
    """
    if sstr == "":
        return None
    sstr = sstr.replace(".", "").replace(",", ".")
    return float(sstr)


class CarteiraBradescoParser(object):

    def __init__(self, caminho, carteira):
        arquivo = open(caminho, 'r')

        self.carteira_xml = BeautifulSoup(arquivo.read(), 'xml')
        self.carteira = carteira

    def parse(self):
        nome_fundo = self.carteira_xml.RELATORIO['NM_CARTEIRA']
        data_carteira = datetime.datetime.strptime(self.carteira_xml.RELATORIO['DT_POSICAO'], '%d/%m/%Y')

        carteira = self.carteira

        self.acoes = self.ler_acoes(self.carteira_xml, carteira)
        self.opcoes = self.ler_opcoes(self.carteira_xml, carteira)
        self.emprestimos = self.ler_emprestimos(self.carteira_xml, carteira)
        self.futuros = self.ler_futuros(self.carteira_xml, carteira)
        self.renda_fixa = self.ler_renda_fixa(self.carteira_xml, carteira)
        self.contas_pagar_receber = self.ler_contas_pagar_receber(self.carteira_xml, carteira)
        self.tesouraria = self.ler_tesouraria(self.carteira_xml, carteira)
        self.cotas_e_patrimonio = self.ler_cotas_e_patrimonio(self.carteira_xml, carteira)
        self.rentabilidade_acumulada = self.ler_rentabilidade_acumulada(self.carteira_xml, carteira)

    def ler_acoes(self, carteira_xml, carteira):

        acoes = []

        bsacoes = carteira_xml.find("ACOES")
        if bsacoes is not None:
            for detalhe in bsacoes.find_all("DETALHE"):
                codigo = detalhe['CODIGO']

                det = {
                    'carteira': carteira,
                    'codigo': codigo,
                    'papel': detalhe['PAPEL'],
                    'disponivel': str_to_float(detalhe['DISPONIVEL']),
                    'bloqueada': str_to_float(detalhe['BLOQUEADA']),
                    'total': str_to_float(detalhe['TOTAL']),
                    'medio': str_to_float(detalhe['MEDIO']),
                    'cotacao': str_to_float(detalhe['COTACAO']),
                    'custo': str_to_float(detalhe['CUSTO']),
                    'resultado': str_to_float(detalhe['RESULTADO']),
                    'mercado_bruto': str_to_float(detalhe['MERCADO_BRUTO']),
                    'irrf': str_to_float(detalhe['IRRF']),
                    'mercado_liquido': str_to_float(detalhe['MERCADO_LIQUIDO']),
                    'p_rv': str_to_float(detalhe['P_RV']),
                    'p_total': str_to_float(detalhe['P_TOTAL'])
                }
                acoes.append(det)

        return acoes

    def ler_opcoes(self, carteira_xml, carteira):

        opcoes = []

        bsopcoes = carteira_xml.find("OPCOES")
        if bsopcoes is not None:
            for detalhe in bsopcoes.find_all("DETALHE"):
                det = {
                    'carteira': carteira,
                    'codigo': detalhe['CODIGO'],
                    'objeto': detalhe['OBJETO'],
                    'tipo': detalhe['TIPO'],
                    'corretora': detalhe['CORRETORA'],
                    'praca': detalhe['PRACA'],
                    'exercicio': str_to_float(detalhe['EXERCICIO']),
                    'vencimento': datetime.datetime.strptime(detalhe['VENCIMENTO'], '%d/%m/%Y %H:%M:%S'),
                    'quantidade': str_to_float(detalhe['QUANTIDADE']),
                    'custo_medio': str_to_float(detalhe['CUSTO_MEDIO']),
                    'cotacao': str_to_float(detalhe['COTACAO']),
                    'custo_total': str_to_float(detalhe['CUSTO_TOTAL']),
                    'resultado': str_to_float(detalhe['RESULTADO']),
                    'valor': str_to_float(detalhe['VALOR']),
                    'p_rv': str_to_float(detalhe['P_RV']),
                    'p_total': str_to_float(detalhe['P_TOTAL']),
                }
                opcoes.append(det)

        return opcoes

    def ler_emprestimos(self, carteira_xml, carteira):

        emprestimos = []

        bsemprestimos = carteira_xml.find("EMPRESTIMO_ACOES")

        if bsemprestimos is not None:
            emprestimos_acoes = bsemprestimos.find("BOLSA")
            if len(emprestimos_acoes) > 0:
                for tipo_movimento in emprestimos_acoes.find_all("TIPO_MOVIMENTO"):
                    movimento = tipo_movimento['MOVIMENTO']
                    tipo = 0 if movimento == u'OperaÃ§Ãµes Doadoras' else 1
                    bolsa = emprestimos_acoes['BOLSA']

                    for detalhe in tipo_movimento.find_all("DETALHE"):

                        codigo_papel = detalhe['CODIGO_PAPEL']

                        ticker_id = None
                        ticker = filter(lambda x: x['ticker'] == codigo_papel, self.tickers)
                        if len(ticker) > 0:
                            ticker_id = ticker[0]['id']

                        det = {
                            'ticker_id': ticker_id,
                            'carteira': carteira,
                            'bolsa': bolsa,
                            'tipo': tipo,
                            'tipo_movimento': movimento,
                            'codigo': str_to_float(detalhe['CODIGO']),
                            'codigo_papel': codigo_papel,
                            'data_operacao': datetime.datetime.strptime(detalhe['DATA_OPERACAO'], '%d/%m/%Y %H:%M:%S'),
                            'financeiro': str_to_float(detalhe['FINANCEIRO']),
                            'nome_papel': detalhe['NOME_PAPEL'],
                            'preco': str_to_float(detalhe['PRECO']),
                            'p_ea': str_to_float(detalhe['P_EA']),
                            'p_mercado': str_to_float(detalhe['P_MERCADO']),
                            'p_remuneracao': str_to_float(detalhe['P_REMUNERACAO']),
                            'p_total': str_to_float(detalhe['P_TOTAL']),
                            'quantidade': str_to_float(detalhe['QUANTIDADE']),
                            'remuneracao': str_to_float(detalhe['REMUNERACAO']),
                            'taxas': str_to_float(detalhe['TAXAS']),
                            'total': str_to_float(detalhe['TOTAL']),
                            'vencimento': datetime.datetime.strptime(detalhe['VENCIMENTO'], '%d/%m/%Y %H:%M:%S')
                        }
                        emprestimos.append(det)

        return emprestimos

    def ler_futuros(self, carteira_xml, carteira):

        futuros = []

        bsfuturos = carteira_xml.find("FUTUROS")

        if bsfuturos is not None:
            for detalhe in bsfuturos.find_all("DETALHE"):
                det = {
                    'carteira': carteira,
                    'ativo': detalhe['ATIVO'],
                    'vencimento': detalhe['VENCIMENTO'],
                    'corretora': detalhe['CORRETORA'],
                    'quantidade': str_to_float(detalhe['QUANTIDADE']),
                    'equalizacao': str_to_float(detalhe['EQUALIZACAO']),
                    'valorizacao': str_to_float(detalhe['VALORIZACAO']),
                    'preco': str_to_float(detalhe['PRECO']),
                    'valor': str_to_float(detalhe['VALOR']),
                    'p_fu': str_to_float(detalhe['P_FU']),
                    'p_total': str_to_float(detalhe['P_TOTAL'])
                }

                futuros.append(det)

        return futuros

    def ler_renda_fixa(self, carteira_xml, carteira):
        rf = []

        bsrenda_fixa = carteira_xml.find("RENDA_FIXA")
        if bsrenda_fixa is not None:
            renda_fixa = bsrenda_fixa.find_all("TIPO_PAPEL")

            for papel in renda_fixa:
                tipo_papel = papel['NOME']

                for detalhe in papel.find_all("DETALHE"):
                    det = {
                        'carteira': carteira,
                        'nome': tipo_papel,
                        'codigo': detalhe['CODIGO'],
                        'aplicacao': datetime.datetime.strptime(detalhe['APLICACAO'], '%d/%m/%Y %H:%M:%S'),
                        'emitente': detalhe['EMITENTE'],
                        'mtm': str_to_float(detalhe['MTM']),
                        'over': str_to_float(detalhe['OVER']),
                        'val_indexador': str_to_float(detalhe['VAL_INDEXADOR']),
                        'indexador': detalhe['INDEXADOR'],
                        'emissao': datetime.datetime.strptime(detalhe['EMISSAO'], '%d/%m/%Y %H:%M:%S'),
                        'vencimento': datetime.datetime.strptime(detalhe['VENCIMENTO'], '%d/%m/%Y %H:%M:%S'),
                        'quantidade': str_to_float(detalhe['QUANTIDADE']),
                        'pu': str_to_float(detalhe['PU']),
                        'valor_aplicacao': str_to_float(detalhe['VALOR_APLICACAO']),
                        'valor_bruto': str_to_float(detalhe['VALOR_BRUTO']),
                        'impostos': str_to_float(detalhe['IMPOSTOS']),
                        'valor_liquido': str_to_float(detalhe['VALOR_LIQUIDO']),
                        'p_rf': str_to_float(detalhe['P_RF']),
                        'p_total': str_to_float(detalhe['P_TOTAL']),
                    }

                    rf.append(det)

        return rf

    def ler_contas_pagar_receber(self, carteira_xml, carteira):
        contas_pagar_receber = []

        contas = carteira_xml.find("CONTAS_PAGAR_RECEBER")
        if contas is not None:
            for detalhe in contas.find_all("DETALHE"):
                det = {
                    'carteira': carteira,
                    'descricao': detalhe['DESCRICAO'],
                    'p_scpr': str_to_float(detalhe['P_SCPR']),
                    'p_stotal': str_to_float(detalhe['P_STOTAL']),
                    'valor': str_to_float(detalhe['VALOR'])
                }
                contas_pagar_receber.append(det)

        return contas_pagar_receber

    def ler_tesouraria(self, carteira_xml, carteira):
        tesouraria = []

        bstesouraria = carteira_xml.find("TESOURARIA")
        if bstesouraria is not None:
            for detalhe in bstesouraria.find_all("DETALHE"):
                det = {
                    'carteira': carteira,
                    'descricao': detalhe['DESCRICAO'],
                    'p_tes': str_to_float(detalhe['P_TES']),
                    'p_total': str_to_float(detalhe['P_TOTAL']),
                    'valor': str_to_float(detalhe['VALOR'])
                }
                tesouraria.append(det)

        return tesouraria

    def ler_cotas_e_patrimonio(self, carteira_xml, carteira):
        dados = {'patrimonio': str_to_float(carteira_xml.find("PATRIMONIO").find("DETALHE")['VALOR'])}

        bsrentabilidade = carteira_xml.find("RENTABILIDADE_ACUMULADA")

        if bsrentabilidade is not None:
            for i in bsrentabilidade.find_all("INDEXADOR"):
                if i['NOME'] == u"Valor da Cota Bruta de Performance":
                    dados['cota_bruta_performance'] = str_to_float(i['PC_BENCHMARK'])
                elif i['NOME'] == u"Quantidade de Cotas (LÃ­quida)":
                    dados['quantidade_cotas'] = str_to_float(i['PC_BENCHMARK'])
                elif i['NOME'] == u"Valor da cota unitÃ¡ria (LÃ­quida)":
                    dados['cota_liquida_performance'] = str_to_float(i['PC_BENCHMARK'])

        dados['carteira'] = carteira

        return dados

    def ler_rentabilidade_acumulada(self, carteira_xml, carteira):
        rentabilidade_acumulada = []

        bsrentabilidade = carteira_xml.find("RENTABILIDADE_ACUMULADA")
        if bsrentabilidade is not None:
            for detalhe in bsrentabilidade.find_all("DETALHE"):
                det = {
                    'carteira': carteira,
                    'indexador': detalhe['INDEXADOR'],
                    'benchmark': str_to_float(detalhe['BENCHMARK']),
                    'rentabilidade': str_to_float(detalhe['RENTABILIDADE']),
                    'diaria': str_to_float(detalhe['DIARIA']),
                    'mensal': str_to_float(detalhe['MENSAL']),
                    'anual': str_to_float(detalhe['ANUAL']),
                    'meses_6': str_to_float(detalhe['MESES_6']),
                    'meses_12': str_to_float(detalhe['MESES_12'])
                }
                rentabilidade_acumulada.append(det)

        return rentabilidade_acumulada
