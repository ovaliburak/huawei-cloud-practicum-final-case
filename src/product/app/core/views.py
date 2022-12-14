from django.shortcuts import render
from rest_framework.generics import ListAPIView
from core.serializers import ProductSerializer
from core.serializers import AdvertList
from core.models import Product
from core.models import Advert
class ProductListAPIView(ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class AdvertListAPIView(ListAPIView):
    serializer_class=AdvertList
    queryset=Advert.objects.all()