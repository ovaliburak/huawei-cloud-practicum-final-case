from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("ex/", views.CreateCustomerView.as_view()),
    path("customer_list/", views.ListCustomerView.as_view()),
    path("create_product/", views.CreateProductView.as_view()),
    path("product_list/", views.ListProductView.as_view()),
    path("create_advert/", views.CreateAdvertView.as_view()),
    path("advert_list/", views.ListAdvertView.as_view()),
    path("create_history/", views.CreateHistoryView.as_view()),
    path("history_list/", views.ListHistoryView.as_view()),
    path("create_demand/", views.CreateDemandView.as_view()),

]
