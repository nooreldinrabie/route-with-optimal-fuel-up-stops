import pandas as pd
import googlemaps
import time

fuel_data =  pd.read_csv('fuel-prices-for-be-assessment.csv')

gmaps = googlemaps.Client(key= 'AIzaSyD6_qASuglbImrpjzfBMCswGzgxgwzPr1g')


def get_coordinates(address):
    """
    The function takes an address and extracts the coordinates

    Args:

        - address (str): the written address

    Returns:

        - coordinates (tuple) : address latitude and longitude 
    """
    try:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None,None

    except Exception as e:
        print(f"Error geocoding {address}: {e}")
        return None, None

latitude = []
longitude = []

for index, row in fuel_data.iterrows():
    address = f"{row['Address']}, {row['City']}, {row['State']}"
    lat, lon = get_coordinates(address)
    latitude.append(lat)
    longitude.append(lon)
    
    
    time.sleep(0.05)

fuel_data['Latitude'] = latitude
fuel_data['Longitude'] = longitude

fuel_data.to_csv('fuel_data.csv', index= False)
print(fuel_data.head())