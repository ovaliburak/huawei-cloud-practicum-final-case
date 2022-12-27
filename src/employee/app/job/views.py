from django.shortcuts import get_object_or_404, render
from rest_framework.schemas.coreapi import serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response, Serializer
from job.serializers import JobSerializer
from job.models import JobApplication

'''
class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    serializer_class= JobSerializer
    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        print(file_obj)
        # do some stuff with uploaded file
        # ...
        return Response(status=204i)

'''
class FileUploadView(ViewSet):
    serializer_class = JobSerializer
    querystet=JobApplication.objects.all()
    

    def list(self, request):
        queryset=JobApplication.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        # file_uploaded = request.FILES.get('upload_file')
        serializer=JobSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('succ')

# Create your views here.
