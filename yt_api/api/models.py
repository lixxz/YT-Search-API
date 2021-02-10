from django.db import models

class SearchResult(models.Model):
    video_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100, db_index=True) # Max YouTube title is 100 chars
    description = models.TextField(db_index=True)
    thumbnail_default_url = models.URLField(null=False)
    thumbnail_medium_url = models.URLField(null=False)
    thumbnail_high_url = models.URLField(null=False)
    published_at = models.DateTimeField(null=False, db_index=True)