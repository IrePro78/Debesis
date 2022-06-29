import os
from celery import Celery
from celery.utils.log import get_task_logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debesisAPI.settings')

app = Celery('debesisAPI')

app.config_from_object('django.conf:settings', namespace='CELERY')

logger = get_task_logger(__name__)

app.autodiscover_tasks()


@app.task(bind=True)
def add():
    logger.info('sdsdsdsdsd')

    return 'ok'
