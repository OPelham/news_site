from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/news/')


@app.route('/news/')
def news():
    articles = call_news()
    return render_template('news.html', articles=articles)


def call_news():
    custom_headers = {"x-api-key": "59bceb20876d4a8f97bb58762a79b86a"}
    news_request = requests.get("https://newsapi.org/v2/everything?domains=rnz.co.nz,cnn.com,bbc.com,dw.com&pagesize=100&language=en", headers=custom_headers)
    news_response_json = dict(news_request.json())
    articles = news_response_json.get("articles")
    return articles


@app.route('/technology/')
def technology():
    tech_articles = call_technology()
    return render_template('news.html', articles=tech_articles)


def call_technology():
    custom_headers = {"x-api-key": "59bceb20876d4a8f97bb58762a79b86a"}
    news_request = requests.get("https://newsapi.org/v2/top-headlines?category=technology&pagesize=100&language=en", headers=custom_headers)
    news_response_json = dict(news_request.json())
    articles = news_response_json.get("articles")
    return articles


@app.route('/business/')
def business():
    business_articles = call_business()
    return render_template('news.html', articles=business_articles)


def call_business():
    custom_headers = {"x-api-key": "59bceb20876d4a8f97bb58762a79b86a"}
    business_request = requests.get("https://newsapi.org/v2/top-headlines?category=business&pagesize=100&language=en", headers=custom_headers)
    news_response_json = dict(business_request.json())
    articles = news_response_json.get("articles")
    return articles


@app.route('/sport/')
def sport():
    sport_articles = call_sport()
    return render_template('news.html', articles=sport_articles)


def call_sport():
    custom_headers = {"x-api-key": "59bceb20876d4a8f97bb58762a79b86a"}
    sport_request = requests.get("https://newsapi.org/v2/top-headlines?category=sport&pagesize=100&language=en", headers=custom_headers)
    news_response_json = dict(sport_request.json())
    articles = news_response_json.get("articles")
    return articles

if __name__ == "__main__":
    app.run(debug=True)