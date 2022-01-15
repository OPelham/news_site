import requests

import hidden_space
# import os

WEATHER_API_KEY = hidden_space.WEATHER_API_KEY
# WEATHER_API_KEY = os.environ.get("WEATHER_KEY")


def enquire_current_weather():
    """Calls OpenWeatherMap API for current weather in specified location.
    Returns a dictionary containing only required fields"""
    location_default = "Rangiora"
    global WEATHER_API_KEY
    _API_key = WEATHER_API_KEY
    _end_point_base = "https://api.openweathermap.org/data/2.5/weather?q={}, NZ&appid={}&units=metric"
    end_point = _end_point_base.format(location_default, _API_key)
    weather_response = requests.get(end_point).json()

    current_weather = process_current_weather(weather_response)
    return current_weather


def process_current_weather(response_info: dict):
    """Process given response dictionary and returns simplified dictionary including only required fields"""

    location = response_info.get("name")
    weather_type = (response_info.get("weather"))[0].get("main")
    _weather_icon = (response_info.get('weather'))[0].get('icon')
    _weather_icon_url_base = "http://openweathermap.org/img/w/{}.png"
    weather_icon_url = _weather_icon_url_base.format(_weather_icon)
    current_temperature = (response_info.get("main")).get("temp")
    max_temperature = (response_info.get("main")).get("temp_max")
    min_temperature = (response_info.get("main")).get("temp_min")
    cloud_cover = (response_info.get("clouds")).get("all")
    humidity = (response_info.get("main")).get("humidity")
    pressure = (response_info.get("main")).get("pressure")
    wind_speed = (response_info.get("wind")).get("speed")
    wind_bearing = (response_info.get("wind")).get("deg")
    wind_gust = (response_info.get("wind")).get("gust")

    current_weather = {
        "location": location,
        "weather_type": weather_type,
        "weather_icon_url": weather_icon_url,
        "current_temperature": current_temperature,
        "max_temperature": max_temperature,
        "min_temperature": min_temperature,
        "cloud_cover": cloud_cover,
        "humidity": humidity,
        "pressure": pressure,
        "wind_speed": wind_speed,
        "wind_bearing": wind_bearing,
        "wind_gust": wind_gust
    }

    return current_weather


def enquire_7_day_forcast():
    location_default = "2192362"  # how get this from user? and how marry to id for call
    global WEATHER_API_KEY
    _API_key = WEATHER_API_KEY
    _end_point_base = "https://api.openweathermap.org/data/2.5/weather?q={}, NZ&appid={}&units=metric"
    end_point = _end_point_base.format(location_default, _API_key)
    weather_response = requests.get(end_point).json()
