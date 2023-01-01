from rest_framework import serializers
from .models import Demand, Employee, Customer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class DemandListSerializer(serializers.ModelSerializer):
    employee=EmployeeSerializer(read_only=True)
    customer=CustomerSerializer(read_only=True)
    class Meta:
        model=Demand
        fields='__all__'

