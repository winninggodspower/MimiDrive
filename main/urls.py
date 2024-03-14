from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car_details/<car_id>/', views.car_detail, name='car_detail'),
    path('collection/', views.collection, name='car_collection'),
    path('collection/search/', views.search, name='search_collection'),
    path('populate-car-data/', views.populate_car_data, name='populate_car_data'),
]