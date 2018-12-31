from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('login/', views.login, name='login'),
    re_path('registration/', views.registration, name='registration'),
]