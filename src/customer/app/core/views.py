from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from core.serializers import CustomerEmployeeListSerializer
from core.models import Customer

class CustomerListAPIView(ListAPIView):
    serializer_class=CustomerEmployeeListSerializer
    queryset = Customer.objects.all()

class CustomerRetrieveAPIView(RetrieveAPIView):
    serializer_class=CustomerEmployeeListSerializer
    queryset=Customer.objects.all()
