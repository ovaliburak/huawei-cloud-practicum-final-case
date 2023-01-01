from django.urls import path
from . import views

urlpatterns=[
    path('history_list/', views.HistoryListAPIView.as_view()),
    path('history_create/', views.HistoryCreateAPIView.as_view()),
]
