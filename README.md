# 🌦️ Weather Dashboard

A simple command-line Python app that fetches real-time weather data using the OpenWeatherMap API.

---

## 🛠️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Install the required Python packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project folder and add your OpenWeatherMap API key:
   ```
   API_KEY=your_openweathermap_api_key
   ```

4. **Run the app**
   ```bash
   python weather.py
   ```

---

## 🧠 Features

- 🌍 Get current weather for any city in the world
- 🌡️ Displays temperature and weather description
- 🔐 API key is hidden using a `.env` file

---

## ⚠️ Notes

- Your `.env` file is **ignored by Git** (see `.gitignore`) to keep your API key safe.
- Make sure you are subscribed to the [OpenWeatherMap Free Plan](https://openweathermap.org/price) to activate your API key.
- It may take a few minutes for new API keys to become active.

---

## 📦 Dependencies

Listed in `requirements.txt`:
- `requests`
- `python-dotenv`

---

## 💡 Future Ideas

- Add a simple GUI (Tkinter or Streamlit)
- Display additional info (humidity, wind, sunrise/sunset)
- Save search history

---

## 📄 License

MIT License (or your preferred license)
