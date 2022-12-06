from django.urls import path
from . import views
urlpatterns=[
path("", views.ExAPI.as_view())
]
