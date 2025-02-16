import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 21.0245,
    "longitude": 105.8412,
    "current": "temperature_2m",
    "timezone": "auto",
}

resp = requests.get(url=url, params=params)

d = 1
