from django.contrib import admin
from cars.models import Car,StateNumberCar,CommentCar, CategoryCar

admin.site.register(Car)
admin.site.register(StateNumberCar)
admin.site.register(CommentCar)
admin.site.register(CategoryCar)
