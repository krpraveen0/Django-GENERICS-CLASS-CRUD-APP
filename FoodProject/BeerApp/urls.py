from django.urls import path
from BeerApp import views

urlpatterns = [
            path("",views.BeerListView.as_view(),name='home'),
            path("detail/<pk>/",views.BeerDetailView.as_view(),name='detail'),
            path("create/",views.BeerCreateView.as_view(),name='create'),
            path("update/<pk>/",views.BeerUpdateView.as_view(),name='update'),
            path("delete/<pk>",views.BeerDeleteView.as_view(),name='delete')
]
