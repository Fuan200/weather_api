from geopy.geocoders import Nominatim

def coordinates(city_name:str) -> tuple[str, str]:
    geolocator = Nominatim(user_agent='uwu')
    location = geolocator.geocode(city_name)

    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude
