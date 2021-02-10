from math import ceil
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import SearchResult
from django.conf import settings


class Query(View):
    def get(self, request):
        data = {}
        if 'q' in request.GET:
            query = request.GET['q']

            page = 1 if 'page' not in request.GET else max(1, int(request.GET['page']))
            # Query should match either title or description. Results are paginated.
            results = SearchResult.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).order_by('-published_at')[(page - 1)* settings.RESULTS_PER_PAGE:page * settings.RESULTS_PER_PAGE]

            data['total_results'] = SearchResult.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).count()

            max_pages = ceil(data['total_results'] / settings.RESULTS_PER_PAGE)
            data['max_results_per_page'] = settings.RESULTS_PER_PAGE
            data['next_page'] = None if page + 1 > max_pages else page + 1
            data['previous_page'] = None if page - 1 < 1 or page - 1 >= max_pages else page - 1
            
            data['results'] = []
            for r in results:
                data['results'].append({'video_id': r.video_id, 'title': r.title, 'description': r.description, 'thumbnail_default_url': r.thumbnail_default_url, 'published_at': r.published_at})
            return JsonResponse(data, status=200)
        else:
            return JsonResponse(data, status=400)


class LatestResults(View):
    def get(self, request):
        data = {}
        page = 1 if 'page' not in request.GET else max(1, int(request.GET['page']))
        results = SearchResult.objects.all().order_by('-published_at')[(page - 1)* settings.RESULTS_PER_PAGE:page * settings.RESULTS_PER_PAGE]

        data['total_results'] = SearchResult.objects.all().count()

        max_pages = ceil(data['total_results'] / settings.RESULTS_PER_PAGE)
        data['max_results_per_page'] = settings.RESULTS_PER_PAGE
        data['next_page'] = None if page + 1 > max_pages else page + 1
        data['previous_page'] = None if page - 1 < 1 or page - 1 >= max_pages else page - 1
        
        data['results'] = []
        for r in results:
            data['results'].append({'video_id': r.video_id, 'title': r.title, 'description': r.description, 'thumbnail_default_url': r.thumbnail_default_url, 'published_at': r.published_at})
        return JsonResponse(data, status=200)
