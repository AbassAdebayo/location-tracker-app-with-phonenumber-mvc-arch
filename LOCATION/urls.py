from django.urls import path
from .views import track_view


urlpatterns = [
    path('track/', track_view, name='track')
]