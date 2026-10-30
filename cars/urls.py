from django.urls import path
from cars.views import car_list_view

urlpatterns = [
    path('cars_list/', car_list_view, name='carsList'),
]