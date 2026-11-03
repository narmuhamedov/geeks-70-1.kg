from django.shortcuts import render, redirect, get_object_or_404
from abituruents.forms import AbiturientsForm
from abituruents.models import Abuturients

#CREATE
def create_abit_view(request):
    if request.method == "POST":
        form_abit = AbiturientsForm(request.POST, request.FILES)
        if form_abit.is_valid():
            form_abit.save()
            return redirect('/abit_list/')
    else:
        form_abit = AbiturientsForm()
    return render(request, 'create_abit.html', {'form': form_abit})

#READ
def abit_list_view(request):
    if request.method == "GET":
        abit_list = Abuturients.objects.all().order_by('-id')
    return render(request, 'abit_list.html', {'abit': abit_list})

#UPDATE
def update_abit_view(request, id):
    abit_id = get_object_or_404(Abuturients, id=id)
    if request.method == "POST":
        form_abit = AbiturientsForm(request.POST, request.FILES, instance=abit_id)
        if form_abit.is_valid():
            form_abit.save()
            return redirect('/abit_list/')
    else:
        form_abit = AbiturientsForm(instance=abit_id)
    return render(request, 'abit_update.html', {'form': form_abit})

#DELETE
def delete_abit_view(request, id):
    abit_id = get_object_or_404(Abuturients, id=id)
    abit_id.delete()
    return redirect('/abit_list/')
