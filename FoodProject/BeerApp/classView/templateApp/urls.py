from django.urls import path
from templateApp import views

urlpatterns = [
    path('',views.TemplateCBV.as_view())
]
