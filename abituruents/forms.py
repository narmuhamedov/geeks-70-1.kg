from django import forms
from abituruents.models import Abuturients

class AbiturientsForm(forms.ModelForm):
    class Meta:
        model = Abuturients
        fields = '__all__'