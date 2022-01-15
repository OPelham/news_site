import requests
import pytz
from datetime import datetime

import hidden_space
# import os

NEWS_API_KEY = hidden_space.NEWS_API_KEY
# NEWS_API_KEY = os.environ.get("NEWS_KEY")


def call_news_api(end_point):
    """Calls NEWS API using the provided endpoint"""
    global NEWS_API_KEY
    custom_headers = {"x-api-key": NEWS_API_KEY}

    news_request = requests.get(end_point, headers=custom_headers)
    news_response_json = dict(news_request.json())
    articles = news_response_json.get("articles")

    convert_date_time(articles)

    return articles


def convert_date_time(articles: dict):
    """Converts UTC time to NZ time for each article of the articles dictionary passed"""
    datetime_format = "%d-%m-%Y | %H:%M"
    for article in articles:
        utc_time_raw = article.get("publishedAt")
        utc_dt = pytz.timezone('UTC').localize(
            datetime(int(utc_time_raw[0:4]), int(utc_time_raw[5:7]), int(utc_time_raw[8:10]), int(utc_time_raw[11:13]),
                     int(utc_time_raw[14:16]), int(utc_time_raw[17:19])))
        local_timezone = pytz.timezone('Pacific/Auckland')
        nz_time = utc_dt.astimezone(local_timezone).strftime(datetime_format)
        article["publishedAt"] = nz_time

    return articles
