from django.shortcuts import render
from rest_framework.generics import ListAPIView
from core.serializers import CustomerEmployeeListSerializer
from core.models import Customer
class CustomerListAPIView(ListAPIView):
    serializer_class=CustomerEmployeeListSerializer
    queryset = Customer.objects.all()
