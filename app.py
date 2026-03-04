import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
ICON_URL = "https://openweathermap.org/img/wn/{icon}@2x.png"


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."
        elif not OPENWEATHER_API_KEY or OPENWEATHER_API_KEY == "your_api_key_here":
            error = "OpenWeatherMap API key is not configured. Please set it in the .env file."
        else:
            try:
                params = {
                    "q": city,
                    "appid": OPENWEATHER_API_KEY,
                    "units": "metric",
                }
                response = requests.get(BASE_URL, params=params, timeout=10)

                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "description": data["weather"][0]["description"].capitalize(),
                        "humidity": data["main"]["humidity"],
                        "wind_speed": data["wind"]["speed"],
                        "icon_url": ICON_URL.format(icon=data["weather"][0]["icon"]),
                    }
                elif response.status_code == 404:
                    error = f"City '{city}' not found. Please check the name and try again."
                else:
                    error = "Unable to fetch weather data. Please try again later."

            except requests.exceptions.ConnectionError:
                error = "Could not connect to the weather service. Check your internet connection."
            except requests.exceptions.Timeout:
                error = "The weather service took too long to respond. Please try again."
            except Exception:
                error = "An unexpected error occurred. Please try again."

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
