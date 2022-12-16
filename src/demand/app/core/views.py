from core import serializers
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from .serializers import DemandListSerializer
from .models import Demand
class DemandListAPIView(ListAPIView):
    serializer_class=DemandListSerializer
    queryset=Demand.objects.all()
class DemandRetrieveAPIView(RetrieveAPIView):
    serializer_class=DemandListSerializer
    queryset=Demand.objects.all()
