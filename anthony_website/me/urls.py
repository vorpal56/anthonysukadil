
from django.urls import path
from me import views

urlpatterns = [
    # path('', views.contactView.as_view(), name='hello_world'),
    path('about/', views.home, name = "about")
]