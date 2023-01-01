from django.db import models


class Employee(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    employee_first_name = models.CharField(max_length=200)
    employee_last_name = models.CharField(max_length=200)
    employee_phone_number = models.CharField(max_length=200)
    employee_is_employee = models.BooleanField(default=False)


class Customer(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    customer_first_name = models.CharField(max_length=200)
    customer_last_name = models.CharField(max_length=200)
    customer_phone_number = models.CharField(max_length=50)


class Demand(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    property_type = models.CharField(max_length=200, blank=True, null=True)
    sqft = models.PositiveIntegerField(blank=True, null=True)
    room_number = models.PositiveIntegerField(blank=True, null=True)
    year_built = models.PositiveIntegerField(blank=True, null=True)
    floor = models.PositiveIntegerField(blank=True, null=True)
    total_floor = models.PositiveIntegerField(blank=True, null=True)
    bathroom_number = models.PositiveIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)

    facade = models.CharField(max_length=10, blank=True, null=True)
    close_to_school = models.BooleanField(default=False)
    close_to_hospital = models.BooleanField(default=False)
    close_to_railway = models.BooleanField(default=False)
    close_to_station = models.BooleanField(default=False)
    close_to_park = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_garage = models.BooleanField(default=False)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee_demand"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_demand"
    )


# Create your models here.
