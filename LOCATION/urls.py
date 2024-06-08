from django.urls import path
from LOCATION.views import track_view


url_patterns = [
    path('track/', track_view, name='track')
]