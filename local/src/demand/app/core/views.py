from core import serializers
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .serializers import DemandListSerializer
from .models import Demand, Employee, Customer
from rest_framework.response import Response

class DemandCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            employee = Employee.objects.get(id=data.get("employee_id"))
        except Employee.DoesNotExist:
            employee = Employee.objects.create(
                id=data.get("employee_id"),
                employee_first_name=data.get("employee_first_name"),
                employee_last_name=data.get("employee_last_name"),
                employee_phone_number=data.get("employee_phone_number"),
            )
            employee.save()
        try:
            customer = Customer.objects.get(customer_phone_number=data.get("customer_phone_number"))
        except Customer.DoesNotExist:
            customer = Customer.objects.create(
                id=data.get("customer_id"),
                customer_first_name=data.get("customer_first_name"),
                customer_last_name=data.get("customer_last_name"),
                customer_phone_number=data.get("customer_phone_number"),
            )
            customer.save()
        try:
            demand = Demand.objects.create(
                property_type=data.get("property_type"),
                sqft=data.get("sqft"),
                room_number=data.get("room_number"),
                year_built=data.get("year_built"),
                floor=data.get("floor"),
                total_floor=data.get("total_floor"),
                bathroom_number=data.get("bathroom_number"),
                price=data.get("price"),
                province=data.get("province"),
                district=data.get("district"),
                facade=data.get("facade"),
                employee=employee, 
                customer=customer
            )
            demand.save()
        except:
            pass
        return Response("Success")
    
class DemandListAPIView(ListAPIView):
    serializer_class=DemandListSerializer
    queryset=Demand.objects.all()
class DemandRetrieveAPIView(RetrieveAPIView):
    serializer_class=DemandListSerializer
    queryset=Demand.objects.all()
