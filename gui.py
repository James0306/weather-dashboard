import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather

def fetch_weather(city_entry, unit_var):
    """
    Retrieves user input from the GUI and fetches the weather information.
    """
    city = city_entry.get()
    units = unit_var.get()
    if city:
        weather = get_weather(city, units)
        messagebox.showinfo("Weather Result", weather)
    else:
        messagebox.showwarning("Input Error", "Please enter a city.")


def run_gui():
    """
    Sets up and runs the weather GUI application.
    """
    root = tk.Tk()
    root.title("Weather App")

    tk.Label(root, text="Enter City:").pack(pady=5)
    city_entry = tk.Entry(root)
    city_entry.pack(pady=5)

    unit_var = tk.StringVar(value="metric")
    tk.Label(root, text="Select Units:").pack()
    tk.Radiobutton(root, text="Celsius (°C)", variable=unit_var, value="metric").pack()
    tk.Radiobutton(root, text="Fahrenheit (°F)", variable=unit_var, value="imperial").pack()

    tk.Button(root, text="Get Weather", command=lambda: fetch_weather(city_entry, unit_var)).pack(pady=10)

    root.mainloop()
