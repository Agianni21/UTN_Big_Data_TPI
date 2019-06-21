import pandas as pd
import re

df = pd.read_csv("crashes.csv")
nuevo = pd.read_csv("data_con_estaciones_mas_nulls.csv")

muestra = df['fatalities']

def printear(valor):
    match = re.match('([0-9]*) .*', valor)
    if match:
        return int(match.group(1))
    return 0

nuevo['fatalities'] = muestra.apply(printear)
nuevo.to_csv('nuevo_csv_supremo.csv')
