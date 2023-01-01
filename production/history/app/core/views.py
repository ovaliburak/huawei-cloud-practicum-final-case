from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import HistorySerializer
from core.models import History
from rest_framework.views import APIView
from rest_framework.response import Response


class HistoryCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        history=History.objects.create(
            product_id=data.get("product_id"),
            customer_id=data.get("customer_id"),
            employee_id=data.get("employee_id"),
            price=data.get("price"))
        history.save()
    
        return Response("Success")
    
class HistoryListAPIView(ListAPIView):
    serializer_class=HistorySerializer
    queryset=History.objects.all()
