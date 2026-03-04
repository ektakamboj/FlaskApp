# Weather App

A Flask web application that lets you search for any city and displays the current weather conditions including temperature, weather icon, humidity, and wind speed.

## Features

- Search weather by city name
- Displays temperature (°C) with "feels like" value
- Weather condition icon from OpenWeatherMap
- Humidity and wind speed details
- Error handling for invalid cities and network issues
- Responsive UI with Bootstrap 5

## Project Structure

```
FlaskApp/
├── .env                  # API key (not committed to git)
├── .env.example          # API key template
├── .gitignore
├── requirements.txt
├── app.py                # Flask entry point
├── static/
│   └── css/
│       └── style.css     # Custom styles
└── templates/
    ├── base.html         # Base layout
    └── index.html        # Search form and weather display
```

## Prerequisites

- Python 3.8 or higher
- A free OpenWeatherMap API key

## Setup

### 1. Clone or download the project

```bash
cd FlaskApp
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **Windows (CMD):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get an OpenWeatherMap API key

1. Go to [https://openweathermap.org/appid](https://openweathermap.org/appid)
2. Sign up for a free account
3. Navigate to **API keys** in your account dashboard
4. Copy your API key

### 5. Configure the API key

Open the `.env` file and set your key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

> **Note:** The free tier key may take a few minutes to activate after creation.

## Running the App

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000` in debug mode.

Open that URL in your browser.

## How to Use

1. Open `http://127.0.0.1:5000` in your browser
2. Type a city name (e.g., **London**, **New York**, **Tokyo**) into the search box
3. Click **Search**
4. The app displays:
   - City name and country code
   - Weather icon representing the current condition
   - Current temperature in °C
   - "Feels like" temperature
   - Weather description (e.g., "Clear sky", "Light rain")
   - Humidity percentage
   - Wind speed in m/s

## Testing the App

### Valid City Search

1. Enter **London** and click Search
2. Verify the result card shows:
   - City: "London, GB"
   - A weather icon image
   - Temperature, humidity, and wind speed values

### Invalid City Search

1. Enter **xyznotacity** and click Search
2. Verify a red error alert appears: *"City 'xyznotacity' not found..."*

### Empty Input

1. Leave the search box empty and click Search
2. Verify the error message: *"Please enter a city name."*

### Missing API Key

1. Remove or clear the key in `.env` (set `OPENWEATHER_API_KEY=`)
2. Restart the app and search for a city
3. Verify the error message about the API key not being configured

### Different Cities

Try searching for cities with spaces or special characters:
- **New York**
- **São Paulo**
- **Los Angeles**
- **Tel Aviv**

All should return valid weather results.

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` |
| "API key is not configured" error | Ensure `.env` has a valid key and restart the app |
| City not found for valid city | API key may not be activated yet — wait a few minutes |
| Connection error | Check your internet connection |

## Tech Stack

- **Flask** — Python web framework
- **Requests** — HTTP client for API calls
- **python-dotenv** — Environment variable management
- **Bootstrap 5** — Responsive UI styling
- **OpenWeatherMap API** — Weather data and icons
