from django.urls import path
from . import views

urlpattersn = [
    path('about_me/', views.about_me),
    path('', views.landing),
]