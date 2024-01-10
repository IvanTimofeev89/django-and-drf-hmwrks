from django.urls import path
from django.contrib import admin

from .views import RetrieveUpdateSensorApi, CreateMeasurementApi, ListCreateSensor

urlpatterns = (
    path('v1/sensors/', ListCreateSensor.as_view()),
    path('v1/sensor/<int:pk>/', RetrieveUpdateSensorApi.as_view()),
    path('v1/add_measurement/', CreateMeasurementApi.as_view()),

)
