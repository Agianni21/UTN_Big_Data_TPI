import pandas as pd
from datetime import date
import re

df = pd.read_csv('best_data.csv')

print(date(2000, 12, 1) < date(2001, 1, 1))

def get_season(row):
    d = row['date']
    lat = int(row['latitude'])
    match = re.match('(.*)-(.*)-(.*)', d)
    year = int(match.group(1))
    month = int(match.group(2))
    day = int(match.group(3))
    fecha = date(year, month, day)

    if lat == -999:
        return "no ubicacion"
    
    invierno = date(year, 6, 21)
    primavera = date(year, 9, 21)
    verano = date(year, 12, 21)
    oto = date(year, 3, 21)
    invierno2 = date(year+1, 6, 21)
    primavera2 = date(year+1, 9, 21)
    verano2 = date(year+1, 12, 21)
    oto2 = date(year+1, 3, 21)

    if lat > 0:
        invierno = date(year, 12, 21)
        primavera = date(year, 3, 21)
        verano = date(year, 6, 21)
        oto = date(year, 9, 21)
        invierno2 = date(year+1, 12, 21)
        primavera2 = date(year+1, 3, 21)
        verano2 = date(year+1, 6, 21)
        oto2 = date(year+1, 9, 21)
        if primavera <= fecha and fecha < verano:
            return "pri"
        if verano <= fecha and fecha < oto:
            return "ver"
        if oto <= fecha and fecha < invierno:
            return "oto"
        return "inv"
    if invierno <= fecha and fecha < primavera:
        return "inv"
    if primavera <= fecha and fecha < verano:
        return "pri"
    if oto <= fecha and fecha < invierno:
        return "oto"
    return "ver"
    
df['estacion'] = df.apply(get_season, axis=1)
del df['Unnamed: 0']
df.to_csv("pruebita.csv")





