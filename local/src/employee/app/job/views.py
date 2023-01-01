from django.shortcuts import get_object_or_404, render
from rest_framework.schemas.coreapi import serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response, Serializer
from job.serializers import JobSerializer
from job.models import JobApplication
from .huawei import modelart
from rest_framework.exceptions import APIException
import json
class FileUploadView(ViewSet):
    serializer_class = JobSerializer
    querystet=JobApplication.objects.all()
    

    def list(self, request):
        queryset=JobApplication.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data.get("first_name"))
        if request.data.get("first_name") == "Practicum":
            raise APIException("There was a problem! Upload valid Resume!")
        else:
            return Response('success')   
    
class FileUploadViewCV(ViewSet):
    serializer_class = JobSerializer
    querystet=JobApplication.objects.all()
    

    def list(self, request):
        queryset=JobApplication.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer=JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Success')   

# Create your views here.
