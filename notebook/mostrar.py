import pandas as pd

df = pd.read_csv("data_con_estaciones_mas_nulls.csv")

muestra = df[['aboard','fatalities','estacion']]
print(muestra.groupby(['estacion']).sum())
