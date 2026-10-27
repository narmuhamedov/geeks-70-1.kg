from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog

def blog_list_view(request):
    if request.method == "GET":
        blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog_list.html', {'blog': blog})

def blog_detail_view(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})






def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('😁Hello World😁')



def image_view(request):
    if request.method == "GET":
        return HttpResponse("<p></p><img src='https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80'> <p>vdsvsdv</p> ")
