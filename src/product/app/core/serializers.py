from rest_framework import serializers
from core.models import Product, Employee, Advert
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class AdvertList(serializers.ModelSerializer):
    employee=EmployeeSerializer(read_only=True)
    product=ProductSerializer(read_only=True)
    class Meta:
        model=Advert
        fields='__all__'