from django.urls import path
from trains.views import *

urlpatterns = [
    path('', TrainListView.as_view(), name='home'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),  # целое число в переменную pk
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('add/', TrainCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
]