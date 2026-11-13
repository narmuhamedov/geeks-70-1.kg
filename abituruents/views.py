from django.shortcuts import render, redirect, get_object_or_404
from abituruents.forms import AbiturientsForm
from abituruents.models import Abuturients

from django.views import generic


#CREATE
class CreateAbitView(generic.CreateView):
    template_name = 'create_abit.html'
    form_class = AbiturientsForm
    success_url = '/abit_list/'

    def form_valid(self, form):
        return super(CreateAbitView, self).form_valid(form=form)


# def create_abit_view(request):
#     if request.method == "POST":
#         form_abit = AbiturientsForm(request.POST, request.FILES)
#         if form_abit.is_valid():
#             form_abit.save()
#             return redirect('/abit_list/')
#     else:
#         form_abit = AbiturientsForm()
#     return render(request, 'create_abit.html', {'form': form_abit})

#READ

class AbitListView(generic.ListView):
    template_name = 'abit_list.html'
    context_object_name = 'abit'
    model = Abuturients
    ordering = ('-id')

    def get_queryset(self):
        return self.model.objects.all().order_by(self.ordering)


# def abit_list_view(request):
#     if request.method == "GET":
#         abit_list = Abuturients.objects.all().order_by('-id')
#     return render(request, 'abit_list.html', {'abit': abit_list})

#UPDATE
class UpdateAbitView(generic.UpdateView):
    template_name = 'abit_update.html'
    model = Abuturients
    form_class = AbiturientsForm
    success_url = '/abit_list/'

    def get_object(self, **kwags):
        abit_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=abit_id)

    def form_valid(self, form):
        return super(UpdateAbitView, self).form_valid(form=form)
        
    
    

# def update_abit_view(request, id):
#     abit_id = get_object_or_404(Abuturients, id=id)
#     if request.method == "POST":
#         form_abit = AbiturientsForm(request.POST, request.FILES, instance=abit_id)
#         if form_abit.is_valid():
#             form_abit.save()
#             return redirect('/abit_list/')
#     else:
#         form_abit = AbiturientsForm(instance=abit_id)
#     return render(request, 'abit_update.html', {'form': form_abit})

#DELETE
class DeleteAbitView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'abit_id'
    success_url = '/abit_list/'
    model = Abuturients

    def get_object(self, **kwags):
        abit_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=abit_id)
        



# def delete_abit_view(request, id):
#     abit_id = get_object_or_404(Abuturients, id=id)
#     abit_id.delete()
#     return redirect('/abit_list/')
