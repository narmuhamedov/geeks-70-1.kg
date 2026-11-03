from django.urls import path
from abituruents.views import create_abit_view, update_abit_view, abit_list_view, delete_abit_view

urlpatterns = [
    path('create_abit/', create_abit_view, name='add_abit'),
    path('abit_list/', abit_list_view, name='abit_list'),
    path('abit_list/<int:id>/edit/', update_abit_view, name='update_abit'),
    path('abit_list/<int:id>/drop/', delete_abit_view, name='drop_abit'),
]
