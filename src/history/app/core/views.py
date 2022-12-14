from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import HistorySerializer
from core.models import History
class HistoryListAPIView(ListAPIView):
    serializer_class=HistorySerializer
    queryset=History.objects.all()
