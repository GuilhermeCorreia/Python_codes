# coding=utf-8
import conexao


class Queries(object):
    """
    Classe com queries mais utilizadas no projeto

    Modo de uso
    Queries.tickers() - retorna um frame com o resultado da query
    """

    conexao = conexao.Conexao()

    @staticmethod
    def tickers():
        """Função que retorna a lista de ticker, ticker_id e empresa_id

        Returns:
            pd.DataFrame()
        """
        sql = "select id, ticker, empresa_id from assets_ticker"
        return Queries.conexao.query(sql)

    @staticmethod
    def valor_mercado():
        """Função que retorna o valor de mercado das empresas

        Returns:
            pd.DataFrame()
        """
        sql = "select empresa_id, ticker_id, date, valor from assets_valormercado"
        return Queries.conexao.query(sql)

    @staticmethod
    def precos_ajustado():
        """Função que retorna o preço de fechamento e preço médio ajustado das empresas

        Returns:
            pd.DataFrame()
        """
        sql = "select date, ticker_id, preult, premed from assets_precohistoricoajustado"
        return Queries.conexao.query(sql)

    @staticmethod
    def precos_nao_ajustado():
        """Função que retorna o volume e o preço de fechamento não ajustado das empresas

        Returns:
            pd.DataFrame()
        """
        sql = "select date, ticker_id, voltot, preult from assets_historicalprice where tpmerc=10"
        return Queries.conexao.query(sql)

    @staticmethod
    def volume_mercado():
        """Função que retorna as informações da tabela volumemercado
        Essas informações são utilizadas para compor o backtest.

        Returns:
            pd.DataFrame()
        """
        sql = "select * from assets_volumemercado"
        return Queries.conexao.query(sql)

    @staticmethod
    def patrimonio_liquido():
        """Função que retorna o patrimônio líquido das empresas

        Returns:
            pd.DataFrame()
        """
        sql = "select empresa_id, ticker_id, date, data_de_divulgacao, valor from assets_patrimonioliquido"
        return Queries.conexao.query(sql)

    @staticmethod
    def lucros():
        """Função que retorna o lucro líquido das empresas

        Returns:
            pd.DataFrame()
        """
        sql = "select ticker_id, empresa_id, date, lucro_liquido from assets_informacoesfinanceiras " \
              "order by empresa_id, date"
        return Queries.conexao.query(sql)

    @staticmethod
    def pesos():
        """Função que retorna os pesos de otimização

        Returns:
            pd.DataFrame()
        """
        sql = "select * from pandas_pesos"
        return Queries.conexao.query(sql)
