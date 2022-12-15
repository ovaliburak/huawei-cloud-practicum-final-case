from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView 
from core.serializers import ProductSerializer
from core.serializers import AdvertListSerializer
from core.models import Product
from core.models import Advert
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
