from django.urls import path
from . import views

urlpatterns = [
    path("product_list/", views.ProductListAPIView.as_view()),
    path("advert_list/", views.AdvertListAPIView.as_view()),
    path("product/<str:pk>/", views.ProductRetrieveAPIView.as_view()),
    path("advert/<str:pk>/", views.AdvertRetrieveAPIView.as_view()),

]
