from django.forms import fields
from BeerApp.models import Beer
from django import forms

class BeerForm(models.ModelForm):
    class Meta:
        model=Beer
        fields = '__all__'
