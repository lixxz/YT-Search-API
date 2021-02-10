import requests
import random
from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone
from .models import SearchResult
from celery import shared_task

@shared_task
def fetch_latest_yt_videos():
    params = {'part': 'snippet', 'type': 'video', 'q': random.choice(settings.SEARCH_QUERIES), 'maxResults': '50', 'publishedAfter': (timezone.now() - timedelta(seconds=settings.FETCH_INTERVAL)).strftime('%Y-%m-%dT%H:%M:%SZ'), 'order': 'date'}
    for key in settings.DEVELOPER_KEYS:
        params['key'] = key
        r = requests.get(settings.API_URL, params=params)
        response_body = r.json()
        if r.status_code == 200:
            results = []
            for items in response_body['items']:
                video_id = items['id']['videoId']
                title = items['snippet']['title']
                description = items['snippet']['description']
                thumbnail_default_url = items['snippet']['thumbnails']['default']['url']
                thumbnail_medium_url = items['snippet']['thumbnails']['medium']['url']
                thumbnail_high_url = items['snippet']['thumbnails']['high']['url']
                published_at = datetime.strptime(items['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.now().tzinfo)
                results.append(SearchResult(video_id=video_id, title=title, description=description,
                thumbnail_default_url=thumbnail_default_url, thumbnail_medium_url=thumbnail_medium_url, 
                thumbnail_high_url=thumbnail_high_url, published_at=published_at))
            SearchResult.objects.bulk_create(results)
        elif r.status_code == 403 and 'quota' in response_body['error']['message']:
            continue
        break
