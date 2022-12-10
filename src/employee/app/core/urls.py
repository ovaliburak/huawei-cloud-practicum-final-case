from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("ex/", views.CreateCustomerView.as_view()),
    path("customer_list/", views.ListCustomerView.as_view())
]
