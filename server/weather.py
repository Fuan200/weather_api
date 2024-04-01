from fastapi import APIRouter, HTTPException
from requests import get

from server.get_coordinates import coordinates
from server.get_api_key import get_api_key

weather = APIRouter()

@weather.get('/weather/{city}')
async def get_weather(city:str):
    lat, lon = coordinates(city)
    lat = "40.7127281"
    lon = "-74.0060152"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={get_api_key()}'
    
    response = get(url)
    data = response.json()
    return data