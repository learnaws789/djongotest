from django.urls import path

from app import views

urlpatterns = [
    path('test_api/', views.test_api),
    path('test_api2/', views.test_api2),

]