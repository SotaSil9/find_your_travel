from django.contrib import admin
from django.urls import path
from cities.views import *

urlpatterns = [
    path('', CityListView.as_view(), name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),  # целое число в переменную pk
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),

]