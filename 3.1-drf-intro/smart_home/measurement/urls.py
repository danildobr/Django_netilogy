from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.SensorListCreateView.as_view()),  # GET список, POST создание
    path('sensors/<pk>/', views.SensorRetrieveUpdateView.as_view()),  # GET детали, PATCH обновление
    path('measurements/', views.MeasurementCreateView.as_view()),  # POST добавление измерения
]