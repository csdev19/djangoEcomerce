from django.contrib.auth.views import login, logout
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path("login", login, {'template_name': 'accounts/login.html'}),
    path("logout", logout, {'next_page':'/'})    
]

