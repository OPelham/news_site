from flask import Flask, render_template, redirect
import requests
import pytz
from datetime import datetime
import os
# import hidden_space

# use hidden space when testing on local and environment variables when using heroku
# WEATHER_API_KEY = hidden_space.WEATHER_API_KEY
# NEWS_API_KEY = hidden_space.NEWS_API_KEY
WEATHER_API_KEY = os.environ.get("WEATHER_KEY")
NEWS_API_KEY = os.environ.get("NEWS_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/news/')


@app.route('/news/')
def news():
    end_point = "https://newsapi.org/v2/everything?domains=rnz.co.nz,bbc.com,dw.com,aljazeera.com&pagesize=100&language=en"
    articles = call_news_api(end_point)
    return render_template('news.html', articles=articles, title='headlines')


@app.route('/newzealand/')
def newzealand():
    end_point = "https://newsapi.org/v2/everything?domains=rnz.co.nz,nzherald.co.nz,newshub.co.nz,odt.co.nz,stuff.co.nz&pagesize=100&language=en"
    articles = call_news_api(end_point)
    return render_template('news.html', articles=articles, title='new zealand')


@app.route('/technology/')
def technology():
    end_point = "https://newsapi.org/v2/top-headlines?category=technology&pagesize=100&language=en"
    tech_articles = call_news_api(end_point)
    return render_template('news.html', articles=tech_articles, title='technology')


@app.route('/business/')
def business():
    end_point = "https://newsapi.org/v2/top-headlines?category=business&pagesize=100&language=en"
    business_articles = call_news_api(end_point)
    return render_template('news.html', articles=business_articles, title='business')


@app.route('/sport/')
def sport():
    end_point = "https://newsapi.org/v2/top-headlines?category=sport&pagesize=100&language=en"
    sport_articles = call_news_api(end_point)
    return render_template('news.html', articles=sport_articles, title='sport')


def call_news_api(end_point):
    global NEWS_API_KEY
    custom_headers = {"x-api-key": NEWS_API_KEY}
    news_request = requests.get(end_point, headers=custom_headers)
    news_response_json = dict(news_request.json())
    articles = news_response_json.get("articles")

    datetime_format = "%d-%m-%Y | %H:%M"
    for article in articles:
        utc_time_raw = article.get("publishedAt")
        utc_dt = pytz.timezone('UTC').localize(datetime(int(utc_time_raw[0:4]), int(utc_time_raw[5:7]), int(utc_time_raw[8:10]), int(utc_time_raw[11:13]), int(utc_time_raw[14:16]), int(utc_time_raw[17:19])))
        local_timezone = pytz.timezone('Pacific/Auckland')
        nz_time = utc_dt.astimezone(local_timezone).strftime(datetime_format)
        article["publishedAt"] = nz_time

    return articles


@app.route('/weather/')
def weather():
    current_weather_dictionary = enquire_current_weather()
    return render_template('weather.html', current_weather=current_weather_dictionary, title='weather')


def enquire_current_weather():
    location_default = "Rangiora"
    global WEATHER_API_KEY
    _API_key = WEATHER_API_KEY
    _end_point_base = "https://api.openweathermap.org/data/2.5/weather?q={}, NZ&appid={}&units=metric"
    end_point = _end_point_base.format(location_default, _API_key)
    weather_response = requests.get(end_point).json()

    location = weather_response.get("name")
    weather_type = (weather_response.get("weather"))[0].get("main")
    _weather_icon = (weather_response.get('weather'))[0].get('icon')
    _weather_icon_url_base = "http://openweathermap.org/img/w/{}.png"
    weather_icon_url = _weather_icon_url_base.format(_weather_icon)
    current_temperature = (weather_response.get("main")).get("temp")
    max_temperature = (weather_response.get("main")).get("temp_max")
    min_temperature = (weather_response.get("main")).get("temp_min")
    cloud_cover = (weather_response.get("clouds")).get("all")
    humidity = (weather_response.get("main")).get("humidity")
    pressure = (weather_response.get("main")).get("pressure")
    wind_speed = (weather_response.get("wind")).get("speed")
    wind_bearing = (weather_response.get("wind")).get("deg")
    wind_gust = (weather_response.get("wind")).get("gust")

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


@app.route('/football/')
def football():
    return render_template('football.html')


@app.route('/covid/')
def covid():
    return render_template('covid.html')


@app.route('/quiz/')
def quiz():
    return render_template('quiz.html')



if __name__ == "__main__":
    app.run(debug=True)
