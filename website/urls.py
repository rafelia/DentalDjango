
from django.urls import path
from . import views


urlpatterns = [
        path('', views.home, name="home"), #path('home.html', views.home, name="home") with this command need this address http://localhost:8000/home.html
        path('contact.html', views.contact, name="contact")
]
