from django.urls import path
from . import views

urlpatterns = [
    path('search', views.Query.as_view()),
    path('latest', views.LatestResults.as_view())
]