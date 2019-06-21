import pandas as pd
import re

df = pd.read_csv("crashes.csv")

muestra = df['fatalities']

def printear(valor):
    print(valor)
#    if valor > 50:
#        print(valor)

muestra.apply(printear)
