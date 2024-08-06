import requests

url = "https://official-joke-api.appspot.com/random_joke" # returns a dictionary
jdata = requests.get(url).json()

arr = ["", ""] # empty list
arr[0] = jdata["setup"]
arr[1] = jdata["punchline"]

def joke():
    return arr

