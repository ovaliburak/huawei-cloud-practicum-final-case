from django.utils.text import phone2numeric
from rest_framework import serializers


class CustomerEmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    employee_id = serializers.IntegerField()
    employee_first_name = serializers.CharField(max_length=200)
    employee_last_name = serializers.CharField(max_length=200)
    employee_email = serializers.EmailField()
    employee_phone_number = serializers.CharField(max_length=50)
    employee_is_employee = serializers.BooleanField(default=False)
