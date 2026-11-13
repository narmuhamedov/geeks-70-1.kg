from django.urls import path
from blog.views import HelloWordView, BlogSearchView, ImageView, BlogListView, BlogDetailView

urlpatterns = [
    path('hello/', HelloWordView.as_view(), name='hello'),
    path('image/', ImageView.as_view(), name='image'),

    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_list/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('search/', BlogSearchView.as_view(), name='search')
]