from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from core.serializers import CustomerEmployeeListSerializer
from core.models import Customer, Employee


class CustomerCreateAPIView(APIView):
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
            customer = Customer.objects.get(phone_number=data.get("phone_number"))
        except Customer.DoesNotExist:
            customer = Customer.objects.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                phone_number=data.get("phone_number"),
                employee=employee,
            )
            customer.save()
        return Response("success")
class CustomerListAPIView(ListAPIView):
    serializer_class=CustomerEmployeeListSerializer
    queryset = Customer.objects.all()

class CustomerRetrieveAPIView(RetrieveAPIView):
    serializer_class=CustomerEmployeeListSerializer
    queryset=Customer.objects.all()
