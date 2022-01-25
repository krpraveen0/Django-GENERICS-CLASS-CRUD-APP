from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class TemplateCBV(TemplateView):
    template_name = 'templateApp/home.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name'] = 'apurva'
        context['course'] ='python fullstack'
        return context
