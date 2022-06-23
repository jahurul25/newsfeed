from urllib import response
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    print("sample_task is called. Celery is working...")
    logger.info("The sample task just ran.")