from django.urls import path

from rest_app import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]