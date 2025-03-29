import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from the .env file

API_KEY = os.getenv("API_KEY")
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
    desc = data['weather'][0]['description']
    print(f"🌡️ {temp}°C in {city} — {desc}")
else:
    print(f"⚠️ Error: {response.status_code} — {response.json().get('message')}")
