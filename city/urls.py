from django.conf.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.home, name='home'),
    re_path('listing/', views.list, name='list'),
    # ---------------------Details url ------------------------
    re_path('restaurant-details/(?P<details_id>\d+)/$', views.restaurant_details, name='restaurant_details'),
    re_path('police-station-details/(?P<police_details_id>\d+)/$', views.police_details, name='police_details'),
    re_path('market-details/(?P<market_details_id>\d+)/$', views.market_details, name='market_details'),
    re_path('hospital-details/(?P<hospital_details_id>\d+)/$', views.hospital_details, name='hospital_details'),
    re_path('fort-details/(?P<fort_details_id>\d+)/$', views.fort_details, name='fort_details'),
    # ------------- single model ------------
    re_path('markets/', views.markets, name='market'),
    re_path('forts/', views.forts, name='forts'),
]