from django.urls import path
from . import views
urlpatterns = [
 path("customer_list/", views.CustomerListAPIView.as_view()),
]
