from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog
from django.core.paginator import Paginator
from django.db.models import F

from django.views import generic



class BlogSearchView(generic.ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blog'
    model = Blog


    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context






# def blog_search_view(request):
#     blog = request.GET.get('q', '')
#     if blog:
#         blog = Blog.objects.filter(title__icontains=blog)
#     else:
#         return HttpResponse('Блог не найден')
#     return render(request, 'blog_list.html', {"blog": blog})



class BlogListView(generic.ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blog'
    ordering = ['-id']
    paginate_by = 2
    model = Blog

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = context['page_obj']
        return context





# def blog_list_view(request):
#     if request.method == "GET":
###########query запрос - запрос из базы данных 
#         blog = Blog.objects.all().order_by('-id')
#         paginator_blog = Paginator(blog, 2)
#         page = request.GET.get('page')
#         page_obj = paginator_blog.get_page(page)
#     return render(request, 'blog_list.html', {'blog': page_obj})


class BlogDetailView(generic.DetailView):
    template_name = 'blog_detail.html'
    context_object_name = 'blog_id'
    model = Blog
    pk_url_kwarg = 'id'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_blog = request.session.get('viewed_blog', [])

        if obj.pk not in views_blog:
            self.model.objects.filter(pk=obj.pk).update(views=F('views')+1)
            views_blog.append(obj.pk)
            request.session['views_blog'] = views_blog
            obj.refresh_from_db()
        return obj

   
        





# def blog_detail_view(request, id):
#     if request.method == "GET":
#         blog_id = get_object_or_404(Blog, id=id)
        
#         views_blog = request.session.get('viewed_blog', [])
#         if id not in views_blog:
#             blog_id.views = F("views") + 1
#             blog_id.save()
#             blog_id.refresh_from_db()
#         views_blog.append(id)
#         request.session['viewed_blog'] = views_blog
#     return render(request, 'blog_detail.html', {'blog_id': blog_id})




class HelloWordView(generic.View):
    def get(self, request):
        return HttpResponse('😁Hello World😁')

# def hello_world_view(request):
#     if request.method == "GET":
#         return HttpResponse('😁Hello World😁')



class ImageView(generic.View):
    def get(self, request):
        return HttpResponse("<p></p><img src='https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80'> <p>vdsvsdv</p>")


# def image_view(request):
#     if request.method == "GET":
#         return HttpResponse("<p></p><img src='https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80'> <p>vdsvsdv</p> ")
