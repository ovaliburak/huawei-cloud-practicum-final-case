from django.db import models

class Employee(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    employee_first_name = models.CharField(max_length=200)
    employee_last_name = models.CharField(max_length=200)
    employee_phone_number = models.CharField(max_length=200)
    employee_is_employee = models.BooleanField(default=False)

class Product(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    sold=models.BooleanField(default=False)
    sales=models.BooleanField(default=False)
    property_type=models.CharField(max_length=200)
    sqft=models.PositiveIntegerField(blank=True, null=True)
    room_number=models.PositiveIntegerField()
    year_built=models.PositiveIntegerField()
    floor=models.PositiveIntegerField()
    total_floor=models.PositiveIntegerField()
    bathroom_number=models.PositiveIntegerField()
    price=models.FloatField()
    province=models.CharField(max_length=50)
    district=models.CharField(max_length=50)

    facade=models.CharField(max_length=10)
    close_to_school=models.BooleanField(default=False)
    close_to_hospital=models.BooleanField(default=False)
    close_to_railway=models.BooleanField(default=False)
    close_to_station=models.BooleanField(default=False)
    close_to_park=models.BooleanField(default=False)
    has_security=models.BooleanField(default=False)
    has_garage=models.BooleanField(default=False)

class Advert(models.Model):
    ad_type=models.CharField(max_length=50)
    product=models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_advert")
    advert_price=models.FloatField()
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee_advert")
