from django.urls import path, re_path, include
from job.views import FileUploadView
from rest_framework import routers
from .views import FileUploadView

router = routers.DefaultRouter()
router.register(r'upload', FileUploadView, basename="upload")

urlpatterns = [
path('', include(router.urls)),
]
