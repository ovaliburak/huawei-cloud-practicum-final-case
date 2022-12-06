from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class ExAPI(APIView):
    def get(self, request, format=None):
        return Response("boom")
