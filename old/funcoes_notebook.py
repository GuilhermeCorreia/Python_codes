import pandas as pd


def frame_cdi_diario():
    cdi = pd.read_excel("../dados/estrategias/cdi.xlsx")
    cdi = cdi.rename(columns={'fechamento': 'cdi'})
    cdi.data = cdi.data.apply(lambda x: x.date())
    cdi.cdi = cdi.cdi.apply(lambda x: 0 if x == "-" else x)
    cdi = cdi.rename(columns={'data': 'date'})
    cdi = cdi[(cdi.cdi != 0)]

    return cdi