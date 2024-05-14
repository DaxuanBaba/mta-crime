import re
import pandas as pd

def extract_lat_long(geo_point):
    match = re.search(r'\(([^)]+)', geo_point)
    if match:
        lat_long = match.group(1).split()
        return [float(lat_long[1]), float(lat_long[0])]  # [latitude, longitude]
    return [None, None] 

data = pd.read_csv('ridership_daily_stationID.csv')

data['Georeference'] = data['Georeference'].astype(str)
data['coordinates'] = data['Georeference'].apply(extract_lat_long)

map_data = data[['station_complex', 'borough', 'coordinates']]

map_data.to_csv('station_map_data.csv', index=False)
