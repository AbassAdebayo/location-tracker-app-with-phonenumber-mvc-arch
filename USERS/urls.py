from django.urls import path
from USERS.views import signup_view, login_view, logout_view


url_patterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]