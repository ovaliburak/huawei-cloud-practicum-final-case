from django.urls import path, re_path, include
from job.views import FileUploadView
from rest_framework import routers
from .views import FileUploadView, FileUploadViewCV

router = routers.DefaultRouter()
router.register(r'upload', FileUploadView, basename="upload")
router.register(r'uploadi', FileUploadViewCV, basename="uploadi")

urlpatterns = [
path('', include(router.urls)),
]
