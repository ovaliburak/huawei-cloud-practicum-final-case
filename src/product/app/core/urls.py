from django.urls import path
from . import views

urlpatterns = [
    path("product_list/", views.ProductListAPIView.as_view()),
    path("advert_list/", views.AdvertListAPIView.as_view()),
]
