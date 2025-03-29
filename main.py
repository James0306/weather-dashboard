import requests

API_KEY = "your_new_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    print(f"Current temperature in {city}: {temp}°C, {weather}")
else:
    print(f"Error {response.status_code}: {response.text}")
