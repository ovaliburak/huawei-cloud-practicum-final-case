from django.db import models


class Employee(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    employee_first_name = models.CharField(max_length=200)
    employee_last_name = models.CharField(max_length=200)
    employee_phone_number = models.CharField(max_length=200)
    employee_is_employee = models.BooleanField(default=False)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(unique=True, max_length=100)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
