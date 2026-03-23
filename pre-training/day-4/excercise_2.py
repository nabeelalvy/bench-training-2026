import sys
from fetch_utils import fetch

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle (light)",
    53: "Drizzle (moderate)",
    55: "Drizzle (dense)",
    56: "Freezing drizzle (light)",
    57: "Freezing drizzle (dense)",
    61: "Rain (slight)",
    63: "Rain (moderate)",
    65: "Rain (heavy)",
    66: "Freezing rain (light)",
    67: "Freezing rain (heavy)",
    71: "Snow fall (slight)",
    73: "Snow fall (moderate)",
    75: "Snow fall (heavy)",
    77: "Snow grains",
    80: "Rain showers (slight)",
    81: "Rain showers (moderate)",
    82: "Rain showers (violent)",
    85: "Snow showers (slight)",
    86: "Snow showers (heavy)",
    95: "Thunderstorm (slight or moderate)",
    96: "Thunderstorm with hail (slight)",
    99: "Thunderstorm with hail (heavy)"
}

def pretty_print_weather(data):

    for city in data:
        print(f"\n🌤️ Weather Summary of {city['city_name']}\n")
        print(f"{'City':<15}: {city['city_name']}")
        print(f"{'Temperature':<15}: {city['temperature']}")
        print(f"{'Unit':<15}: {city['temperature_unit']}")
        print(f"{'Wind Speed':<15}: {city['wind_speed']}")
        print(f"{'Wind Speed Unit':<15}: {city['wind_speed_unit']}")
        print(f"{'Condition':<15}: {city['description']}")
        print("-" * 40)


def extract_weather_info(data):
    current = data["current"]
    current_units = data["current_units"]

    temp = current["temperature_2m"]
    temp_unit = current_units["temperature_2m"]
    wind_speed = current["wind_speed_10m"],
    wind_speed_unit = current_units["wind_speed_10m"]
    description = WEATHER_CODES.get(current["weathercode"], "No Description Available")

    return {
        "temperature": f"{temp:.1f}",
        "temperature_unit": temp_unit,
        "wind_speed": wind_speed[0] if len(wind_speed) > 0 else wind_speed,
        "wind_speed_unit": wind_speed_unit,
        "description": description
    }

def get_coordinates(country):
     response = fetch(f"https://geocoding-api.open-meteo.com/v1/search?name={country}")
     if not response or "results" not in response or not response["results"]:
        print("Failed to get city information")
        return None
     return response


def get_temperature_data(city_info_json, unit="C"):
    final_weather_info = []

    if not city_info_json or "results" not in city_info_json:
        return final_weather_info

    for city in city_info_json["results"]:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={city['latitude']}&longitude={city['longitude']}&current=temperature_2m,wind_speed_10m,weathercode"
        if unit == "F":
            url += "&temperature_unit=fahrenheit"
        fetched_weather_info = fetch(url)

        if fetched_weather_info is None:
            raise RuntimeError("Failed to fetch weather data")

        weather_info = extract_weather_info(fetched_weather_info)
        final_weather_info.append({
            "city_name": city.get("admin2", "(City Name not available)"),
            **weather_info
        })
    return final_weather_info


def get_weather_data(country):
    city_info_json = get_coordinates(country)
    if city_info_json is None:
        raise RuntimeError("Failed to fetch coordinates")
    _ = city_info_json["results"].pop(0)

    weather_in_celsius = get_temperature_data(city_info_json)
    weather_in_fahrenheit = get_temperature_data(city_info_json, unit="F")

    return weather_in_celsius, weather_in_fahrenheit

def main():
    location = sys.argv[1] if len(sys.argv) > 1 else "Pakistan"
    print("Fetching weather information for " + location + "...")
    try:
        weather_in_celsius, weather_in_fahrenheit = get_weather_data(location)
        print("\nUnit in Celsius")
        pretty_print_weather(weather_in_celsius)
        print("\nUnit in Fahrenheit")
        pretty_print_weather(weather_in_fahrenheit)
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()