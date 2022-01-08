from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/news/')


@app.route('/news/')
def news():
    end_point = "https://newsapi.org/v2/everything?domains=rnz.co.nz,cnn.com,bbc.com,dw.com,reuters.com&pagesize=100&language=en"
    articles = call_news_api(end_point)
    return render_template('news.html', articles=articles, title='news')


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
    custom_headers = {"x-api-key": "59bceb20876d4a8f97bb58762a79b86a"}
    news_request = requests.get(end_point, headers=custom_headers)
    news_response_json = dict(news_request.json())
    articles = news_response_json.get("articles")
    return articles


@app.route('/weather/')
def weather():
    current_weather_dictionary = enquire_current_weather()
    return render_template('weather.html', current_weather=current_weather_dictionary, title='weather')


def enquire_current_weather():
    location_default = "Rangiora"
    _API_key = "70f646114a0cf8d45f17792318c2950a"
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
    _API_key = "70f646114a0cf8d45f17792318c2950a"
    _end_point_base = "https://api.openweathermap.org/data/2.5/weather?q={}, NZ&appid={}&units=metric"
    end_point = _end_point_base.format(location_default, _API_key)
    weather_response = requests.get(end_point).json()


if __name__ == "__main__":
    app.run(debug=True)
