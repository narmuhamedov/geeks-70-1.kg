from django.shortcuts import render
from django.http import HttpResponse

def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse('😁Hello World😁')



def image_view(request):
    if request.method == "GET":
        return HttpResponse("<p></p><img src='https://img.magnific.com/free-vector/simple-vibing-cat-square-meme_742173-4493.jpg?semt=ais_hybrid&w=740&q=80'> <p>vdsvsdv</p> ")
