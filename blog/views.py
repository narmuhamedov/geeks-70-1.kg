from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog
from django.core.paginator import Paginator
from django.db.models import F



def blog_search_view(request):
    blog = request.GET.get('q', '')
    if blog:
        blog = Blog.objects.filter(title__icontains=blog)
    else:
        return HttpResponse('Блог не найден')
    return render(request, 'blog_list.html', {"blog": blog})




def blog_list_view(request):
    if request.method == "GET":
        blog = Blog.objects.all().order_by('-id')
        paginator_blog = Paginator(blog, 2)
        page = request.GET.get('page')
        page_obj = paginator_blog.get_page(page)
    return render(request, 'blog_list.html', {'blog': page_obj})


def blog_detail_view(request, id):
    if request.method == "GET":
        blog_id = get_object_or_404(Blog, id=id)
        
        views_blog = request.session.get('viewed_blog', [])
        if id not in views_blog:
            blog_id.views = F("views") + 1
            blog_id.save()
            blog_id.refresh_from_db()
        views_blog.append(id)
        request.session['viewed_blog'] = views_blog
    return render(request, 'blog_detail.html', {'blog_id': blog_id})






def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('😁Hello World😁')



def image_view(request):
    if request.method == "GET":
        return HttpResponse("<p></p><img src='https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80'> <p>vdsvsdv</p> ")
