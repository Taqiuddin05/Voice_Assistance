import requests
from ss import *

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" +key
# stores data retrieved from newsapi
json_data = requests.get(api_address).json()
# searches url and convert it to json file

ar = [] # empty list
def news() :
    for i in range(3):
        # running loop for 3 times
        ar.append("Number" +str(i+1) +" "+ json_data["articles"][i]["title"]+".")
    return ar




