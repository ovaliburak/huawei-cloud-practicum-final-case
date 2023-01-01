from django.urls import path
from . import views

urlpatterns = [
    path("customer_list/", views.CustomerListAPIView.as_view()),
    path("customer/<str:pk>/", views.CustomerRetrieveAPIView.as_view()),
    path("customer_create/", views.CustomerCreateAPIView.as_view()),
]
