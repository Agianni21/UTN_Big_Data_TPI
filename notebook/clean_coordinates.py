import pandas as pd
from ast import literal_eval

df = pd.read_csv("data_with_location_tuple.csv")

coordinates = df['coordinates']

def get_latitude(tuple):
    print("lat")
    s = literal_eval(tuple)
    print(s)
    return s[0]

def get_longitude(tuple):
    print("long")
    s = literal_eval(tuple)
    print(s)
    return s[1]

df['latitude'] = df['coordinates'].apply(get_latitude)
df['longitude'] = df['coordinates'].apply(get_longitude)

df.to_csv("data_with_clean_location_tuple.csv")
