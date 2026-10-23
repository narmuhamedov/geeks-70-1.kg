from django.urls import path
from blog.views import hello_world_view, image_view

urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('image/', image_view, name='image'),
]