from django import forms
from .models import Books

class Bookforms(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'