import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str, units: str = "metric") -> str:
    """
    Fetch weather for a given city using OpenWeatherMap API.
    """
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not API_KEY:
        return "Error: API key not found. Please set it in your .env file."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data['main']['temp']
        return f"Temperature in {city}: {temp}° {'C' if units == 'metric' else 'F'}"
    except requests.exceptions.HTTPError:
        return "City not found or API error."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
