
import json
import math
import random
import string
import time
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from core.services import UserService

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        data['is_employee'] = True
        if not request.data.get("password") or not request.data.get("password_confirm"):
            raise exceptions.APIException("Password or Password Confirm must set.") 
        else:
            print(data)
            return Response(UserService.post('register', data=data))


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        data['scope'] = 'employee'

        res = UserService.post('login', data=data)

        response = Response()
        response.set_cookie(key='jwt', value=res['jwt'])
        response.data = {
            'message': 'success'
        }

        return response
    
class LogoutAPIView(APIView):
    def post(self, request):
        data = request.data
        data['scope'] = 'employee'

        UserService.post('logout', data=data, headers=request.headers)

        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            'message': 'success'
        }

        return response
        
