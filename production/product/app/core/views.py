from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from core.serializers import ProductSerializer
from core.serializers import AdvertListSerializer
from core.models import Product
from core.models import Advert
from core.models import Employee

class ProductCreateAPIView(APIView):
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
        product=Product.objects.create(
            property_type=data.get("property_type"),
            sqft=data.get("sqft"),
            room_number=data.get("room_number"),
            year_built=data.get("year_built"),
            floor=data.get("floor"),
            total_floor=data.get("total_floor"),
            bathroom_number=data.get("bathroom_number"),
            price=data.get("price"),
            province=data.get('province'),
            district=data.get('district'),
            facade=data.get("facade")
        )
        product.save()
        return Response("Success")

class AdvertCreateAPIView(APIView):
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
            print(employee)
            employee.save()
        try:
            product = Product.objects.get(id=data.get("product_id"))
        except Product.DoesNotExist:
            product=None
        try:
            advert=Advert.objects.create(
                ad_type=data.get("ad_type"),
                product=product,
                advert_price=data.get("advert_price"),
                employee=employee
            )
            advert.save()
            product.sales=True
            print(product)
            product.save()
        except:
            pass
        
        return Response("Success")


class ProductSoldAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            product = Product.objects.get(id=data.get("product_id"))
            print(product)
            product.sold = True
            product.sales = False
            product.save()
            try:
                Advert.objects.filter(product=product).delete()
            except:
                pass
        except:
            pass
        return Response("Success")
class ProductListAPIView(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class AdvertListAPIView(ListAPIView):
    serializer_class=AdvertListSerializer
    queryset=Advert.objects.all()

class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
class AdvertRetrieveAPIView(RetrieveAPIView):
    serializer_class=AdvertListSerializer
    queryset=Advert.objects.all()
