from django.contrib import admin
from django.urls import path, include


url_patterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('location/', include('location.urls')),
]