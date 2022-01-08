from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/news/')


@app.route('/news/')
def news():
    end_point = "https://newsapi.org/v2/everything?domains=rnz.co.nz,cnn.com,bbc.com,dw.com&pagesize=100&language=en"
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
    end_point = "https://api.openweathermap.org/data/2.5/weather?q=Rangiora, NZ&appid=70f646114a0cf8d45f17792318c2950a&units=metric"
    weather_forcast = call_weather_api(end_point)
    return render_template('weather.html', weather_forcast=weather_forcast, title='weather')


def call_weather_api(end_point):
    weather_response = requests.get(end_point)
    weather_response_json = weather_response.json()
    return weather_response_json
    # map to custom dict instead for readability and maintainability in html. All at one level with key min_temp



if __name__ == "__main__":
    app.run(debug=True)
