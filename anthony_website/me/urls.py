
from django.urls import path
from me import views

urlpatterns = [
    path('', views.home, name='hello_world'),
    path('about/', views.home, name = "about")
]