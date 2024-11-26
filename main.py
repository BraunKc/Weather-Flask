from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")


# city to lat:float and lon:float of city
def get_location(city: str):
    location = geolocator.geocode(city)
    if location is not None:
        lat = location.latitude
        lon = location.longitude
        return lat, lon
    return False

# lat, lon to city:str
def get_city(lat: float, lon: float) -> str:
    address = geolocator.reverse((lat, lon))
    city = address.raw['address']['city']
    return city
