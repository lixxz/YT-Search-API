import os
from celery import Celery
from django.conf import settings 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt_api.settings')

app = Celery('yt_api')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_url = settings.CELERY_BROKER_URL

app.conf.beat_schedule = {
    'fetch-videos-regularly': {
        'task': 'api.tasks.fetch_latest_yt_videos',
        'schedule': settings.FETCH_INTERVAL
    }
}

app.autodiscover_tasks()