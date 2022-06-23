from urllib import response
from celery import shared_task
from celery.utils.log import get_task_logger
import requests, json
# from newsfeedapp import models

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    url = "https://newsapi.org/v2/everything?q=tesla&from=2022-05-22&sortBy=publishedAt&apiKey=880be7984e8546d1a4e4f00471040890"
    response = requests.get(url)
    news = response.json()
    articles = news["articles"]
    print("articles: ", articles)
    # models.NewsInfo.objects.create(source_name="", author="", haeadline="", country_of_news="us")
    print("test: ", response.json())
    print("sample_task is called. Celery is working...")
    logger.info("The sample task just ran.")