from django.urls import path
from . import views
urlpatterns=[
    path("demand_list/", views.DemandListAPIView.as_view()),
    path("demand/<str:pk>/", views.DemandRetrieveAPIView.as_view()),
    path("demand_create/", views.DemandCreateAPIView.as_view()),
]
