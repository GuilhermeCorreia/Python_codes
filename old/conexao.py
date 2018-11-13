# coding=utf-8
from estrategias import conexao
from sqlalchemy import create_engine
import pandas.io.sql as psql


class Conexao(object):
    """Conexao

    Classe que realiza a conexão no banco de dados através do sqlalchemy
    """

    def __init__(self, user=None, password=None, host=None, database=None):
        """
        Attrs:
            _con: Atributo com a conexão do banco de dados
        """

        if user is None and password is None and host is None and database is None:
            user = conexao.USER
            password = conexao.PASSWORD
            host = conexao.HOST
            database = conexao.DATABASE

        self._user = user
        self._password = password
        self._host = host
        self._database = database

        if self._host == '10.0.0.5':
            print "Você está conectando no servidor"
        elif self._host == '127.0.0.1' or self._host == 'localhost':
            print "Você está conectando no localhost"
        else:
            print "Você está conectando em outro computador"

        self.con = create_engine(
            'mysql+mysqldb://%s:%s@%s:3306/%s?charset=utf8' % (self._user, self._password, self._host, self._database),
            echo=False
        )

        print self.__repr__()

    def query(self, query):
        """Método que realiza uma query no banco de dados e retorna um DataFrame

        Args:
            query (str): String contendo a query a ser executada

        Returns:
            frame (pd.DataFrame): Pandas DataFrame contendo o resultado da query
        """
        frame = psql.read_sql(query, con=self.con)
        print query
        return frame

    def __repr__(self):
        return "Conexao <{0}>".format(self.con)
