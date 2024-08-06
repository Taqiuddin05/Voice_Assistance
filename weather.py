import requests
from ss import *
api_address = "https://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=" +key2
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    # temp is in kelvin so we subtract 273
    # we rounded the temp to 1 decimal point
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

