from django.shortcuts import render
from BeerApp.models import Beer
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView

# Create your views here.
#list out all beers:
class BeerListView(ListView):
    model=Beer
    success_url=reverse_lazy('home')

#Deails of a Beer
class BeerDetailView(DetailView):
    model=Beer
    success_url=reverse_lazy('detail')

#creating the beers
class BeerCreateView(CreateView):
    model=Beer
    fields = '__all__'
    success_url=reverse_lazy('home')

#Updation of the Application
class BeerUpdateView(UpdateView):
    model=Beer
    fields='__all__'
    template_name_suffix='_update_form'
    success_url=reverse_lazy('home')

#deleting a beers
class BeerDeleteView(DeleteView):
    model=Beer
    success_url=reverse_lazy('home')
