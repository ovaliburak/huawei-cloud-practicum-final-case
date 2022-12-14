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


class ProductEmployeeSerializer(serializers.Serializer):
    property_type = serializers.CharField(max_length=200)
    sqft = serializers.IntegerField()
    room_number = serializers.IntegerField()
    year_built = serializers.IntegerField()
    floor = serializers.IntegerField()
    total_floor = serializers.IntegerField()
    bathroom_number = serializers.IntegerField()
    price = serializers.FloatField()
    province = serializers.CharField(max_length=50)
    district = serializers.CharField(max_length=50)

    facade = serializers.CharField()
    close_to_school = serializers.BooleanField(default=False)
    close_to_hospital = serializers.BooleanField(default=False)
    close_to_railway = serializers.BooleanField(default=False)
    close_to_station = serializers.BooleanField(default=False)
    close_to_park = serializers.BooleanField(default=False)
    has_security = serializers.BooleanField(default=False)
    has_garage = serializers.BooleanField(default=False)

    employee_id = serializers.IntegerField()
    employee_first_name = serializers.CharField(max_length=200)
    employee_last_name = serializers.CharField(max_length=200)
    employee_email = serializers.EmailField()
    employee_phone_number = serializers.CharField(max_length=50)
    employee_is_employee = serializers.BooleanField(default=False)

class AdvertEmployeeSerializer(serializers.Serializer):
    ad_type=serializers.CharField(max_length=50)
    product_id=serializers.IntegerField()
    advert_price=serializers.FloatField()

    employee_id = serializers.IntegerField()
    employee_first_name = serializers.CharField(max_length=200)
    employee_last_name = serializers.CharField(max_length=200)
    employee_email = serializers.EmailField()
    employee_phone_number = serializers.CharField(max_length=50)
    employee_is_employee = serializers.BooleanField(default=False)


class HistorySerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()
    price=serializers.FloatField()
 
