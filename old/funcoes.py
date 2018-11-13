# coding=utf-8
import calendar
import datetime
import pandas as pd

import cPickle
import os

from dateutil.relativedelta import relativedelta

from helper import feriados


def buscar_dia_anterior(date):
    """Retorna o dia útil anterior"""

    date -= datetime.timedelta(days=1)
    while (date.weekday() == calendar.SATURDAY or date.weekday() == calendar.SUNDAY) or (date in feriados.lista()):
        date -= datetime.timedelta(days=1)
    return date

def net_workdays1(data_inicial, data_final):
    net_days=(data_final-data_inicial).days
    lst=[]
    data=data_inicial
    for i in range (0,net_days):
        data+=datetime.timedelta(days=1)
        lst.append({'fds':data,'weekday':data.weekday()})
    d=pd.DataFrame.from_dict(lst)
    f = len(d[d['weekday']>4])+sum(1 if (x>=data_inicial)&(x<=data_final)&(x not in d['fds']) else 0 for x in pd.to_datetime(feriados.lista()))
    net_days -= f
    return net_days


def proximo_dia_util(date):
    date += datetime.timedelta(days=1)
    while (date.weekday() == calendar.SATURDAY or date.weekday() == calendar.SUNDAY) or (date in feriados.lista()):
        date += datetime.timedelta(days=1)
    return date


def buscar_proximo_dia_util(date):
    """Retorna o próximo dia útil caso o parâmetro não seja dia útil"""

    while (date.weekday() == calendar.SATURDAY or date.weekday() == calendar.SUNDAY) or (date in feriados.lista()):
        date += datetime.timedelta(days=1)
    return date


def get_last_util_day(date):
    """Retorna o último dia útil do mês"""

    try:
        last_day = calendar.monthrange(int(date.year), int(date.month))[1]
        d = datetime.datetime(int(date.year), int(date.month), last_day)
        while d.weekday() == calendar.SATURDAY or d.weekday() == calendar.SUNDAY or (d.date() in feriados.lista()):
            d -= datetime.timedelta(days=1)
        return d.date()
    except Exception as e:
        raise Exception("erro ao buscar ultimo dia util do mes %s" % date)


def primeira_data_mes(date):
    """Retorna o primeiro dia útil do mês"""

    try:
        d = datetime.datetime(int(date.year), int(date.month), 1)
        while d.weekday() == calendar.SATURDAY or d.weekday() == calendar.SUNDAY or (d.date() in feriados.lista()):
            d += datetime.timedelta(days=1)
        return d.date()
    except Exception as e:
        raise Exception("erro ao buscar primeiro dia util do mes %s" % date)


def ultimo_dia_util_holding_period(date, hold_period):
    """Retorna o último dia útil do holding period"""

    data = date + relativedelta(months=hold_period)
    last_day = calendar.monthrange(int(data.year), int(data.month))[1]
    d = datetime.datetime(int(data.year), int(data.month), last_day)
    return get_last_util_day(d)


def buscar_data_proximo_mes(date):
    return ultimo_dia_util_holding_period(date, 1)


def data_tri_para_datetime(row):
    mes = int(row[0:1]) * 3
    ano = int(row[2:6])

    data = datetime.date(ano, mes, 1)
    return ultimo_dia_mes(data)


def ultimo_dia_mes(date):
    """Retorna o último dia do mês"""

    last_day = calendar.monthrange(int(date.year), int(date.month))[1]
    d = datetime.datetime(int(date.year), int(date.month), last_day)
    return d.date()


def datas_carteira_periodo(data_inicial, data_final, holding_period=1):
    """Retorna uma lista de datas com o último dia do mês"""

    datas_carteira = []

    data = data_inicial

    while data <= data_final:
        datas_carteira.append(data)
        data = get_last_util_day(data + relativedelta(months=holding_period))

    return datas_carteira


def exportar_pickle(obj, path):
    """
    Função que exporta arquivo pickle
    Args:
        obj: Objeto a ser exportado
        path: Caminho onde o pickle será salvo

    """
    f = file(path, 'wb')
    cPickle.dump(obj, f, protocol=cPickle.HIGHEST_PROTOCOL)
    f.close()
    print "Pickle exportado."


def importar_pickle(path):
    """
    Função que importa arquivo pickle
    Args:
        path: Caminho onde o arquivo pickle está

    """
    f = file(path, 'rb')
    p = cPickle.load(f)
    f.close()
    print "Pickle importado."
    return p


def buscar_pasta_rebalanceamento(data_rebalanceamento):
    """
    Função que verifica se a pasta do rebalanceamento existe no servidor, se não existir, cria a pasta
    Args:
        data_rebalanceamento (date): Data do rebalanceamento

    """
    path = r'N:\Data Science Project\Fundo\rebalanceamento\{0}'.format(data_rebalanceamento)

    if not os.path.exists(path):
        os.makedirs(path)

    return path
