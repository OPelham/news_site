from flask import Flask, render_template, redirect
from helpers.news_api import call_news_api
from helpers.weather_api import enquire_current_weather

app = Flask(__name__)


@app.route('/')
def index():
    end_point = "https://newsapi.org/v2/everything?domains=rnz.co.nz,bbc.com,dw.com,aljazeera.com&pagesize=9&language=en"
    articles = call_news_api(end_point)
    end_point = "https://newsapi.org/v2/everything?domains=rnz.co.nz,nzherald.co.nz,newshub.co.nz,odt.co.nz,stuff.co.nz&pagesize=100&language=en"
    nz_articles = call_news_api(end_point)
    end_point = "https://newsapi.org/v2/top-headlines?category=technology&pagesize=100&language=en"
    tech_articles = call_news_api(end_point)
    return render_template('home.html', articles=articles, nz_articles=nz_articles, tech_articles=tech_articles)


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


@app.route('/weather/')
def weather():
    current_weather_dictionary = enquire_current_weather()
    return render_template('weather.html', current_weather=current_weather_dictionary, title='weather')


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
