from rest_framework import serializers
from . import models
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Employee
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields = '__all__'
class CustomerEmployeeListSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model=models.Customer
        fields="__all__"
