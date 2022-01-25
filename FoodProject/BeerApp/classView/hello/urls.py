from django.urls import path
from hello import views

urlpatterns = [
    path('',views.HelloWorld.as_view())
]
