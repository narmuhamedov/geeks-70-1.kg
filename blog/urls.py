from django.urls import path
from blog.views import hello_world_view, blog_search_view, image_view, blog_list_view, blog_detail_view

urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('image/', image_view, name='image'),

    path('blog_list/', blog_list_view, name='blog_list'),
    path('blog_list/<int:id>/', blog_detail_view, name='blog_detail'),
    path('search/', blog_search_view, name='search')
]