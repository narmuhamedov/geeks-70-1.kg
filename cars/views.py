from django.shortcuts import render
from cars.models import Car

def car_list_view(request):
    if request.method == "GET":
        car = Car.objects.all().order_by('-id')
    return render(request, 'cars_list.html', {'car': car})