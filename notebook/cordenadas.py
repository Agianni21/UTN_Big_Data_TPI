import pandas as pd

df = pd.read_csv("clean_data.csv")

locations = df['location']

def get_location(string):
    from geopy.geocoders import Nominatim
    import time
    try:
        geolocator = Nominatim(user_agent="ge_data_utn")
        location = geolocator.geocode(string)
        time.sleep(2)
        if location == None:
            print()
            print(string)
            print("FALLO")
            print()
            return (-999 , -999)
        print()
        print(string)
        print("-------")
        print(location.latitude)
        print(location.longitude)
        print()
        return (location.latitude, location.longitude) 
    except:
        print("EXCEPCIONO")
        return (-999 , -999)


df['coordinates'] = df['location'].apply(get_location)

df.to_csv("data_with_location_tuple.csv")
