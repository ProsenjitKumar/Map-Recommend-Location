from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('write-review/', views.write_review, name='write_review'),
]