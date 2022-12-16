import json
import time
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from core.services import UserService
from core.services import CustomerService
from core.services import ProductService
from core.services import HistoryService
from core.producer import publish
from core.serializers import CustomerEmployeeSerializer
from core.serializers import ProductEmployeeSerializer
from core.serializers import AdvertEmployeeSerializer
from core.serializers import HistorySerializer
from core.serializers import DemandSerializer
from django.http import QueryDict

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        data["is_employee"] = True
        if not request.data.get("password") or not request.data.get("password_confirm"):
            raise exceptions.APIException("Password or Password Confirm must set.")
        else:
            print(data)
            return Response(UserService.post("register", data=data))


class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        data["scope"] = "employee"

        res = UserService.post("login", data=data)

        response = Response()
        response.set_cookie(key="jwt", value=res["jwt"])
        response.data = {"message": "success"}

        return response


class LogoutAPIView(APIView):
    def post(self, request):
        data = request.data
        data["scope"] = "employee"

        UserService.post("logout", data=data, headers=request.headers)

        response = Response()
        response.delete_cookie(key="jwt")
        response.data = {"message": "success"}

        return response


class CreateCustomerView(APIView):
    def post(self, request):
        if request.user_ms.get("detail") != "unauthenticated":
            request.data.update({
                "employee_id": request.user_ms.get("id"),
                "employee_first_name": request.user_ms.get("first_name"),
                "employee_last_name":request.user_ms.get("last_name"),
                "employee_email":request.user_ms.get("email"),
                "employee_is_employee":request.user_ms.get("is_employee"),
                "employee_phone_number":request.user_ms.get("phone_number")
            })
            serializer = CustomerEmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            publish("customer_created", "customer",serializer.data)
            return Response("Success")
        else:
            return Response("Authentication Required")
class ListCustomerView(APIView):
    def get(self, request):
        resp = CustomerService.get("customer_list")
        print(resp)
        return Response(resp)

class CreateProductView(APIView):
    def post(self, request):
        if request.user_ms.get("detail") != "unauthenticated":
            request.data.update({
                "employee_id": request.user_ms.get("id"),
                "employee_first_name": request.user_ms.get("first_name"),
                "employee_last_name":request.user_ms.get("last_name"),
                "employee_email":request.user_ms.get("email"),
                "employee_is_employee":request.user_ms.get("is_employee"),
                "employee_phone_number":request.user_ms.get("phone_number")
            })
            serializer = ProductEmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            publish("product_created", "product", serializer.data)
            return Response("Success")
        else:
            return Response("Authentication Required")


class CreateAdvertView(APIView):
    def post(self, request):
        if request.user_ms.get("detail") != "unauthenticated":
            request.data.update({
                "employee_id": request.user_ms.get("id"),
                "employee_first_name": request.user_ms.get("first_name"),
                "employee_last_name":request.user_ms.get("last_name"),
                "employee_email":request.user_ms.get("email"),
                "employee_is_employee":request.user_ms.get("is_employee"),
                "employee_phone_number":request.user_ms.get("phone_number")
            })
            serializer = AdvertEmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            publish("advert_created", "product", serializer.data)
            return Response("Success")
        else:
            return Response("Authentication Required")

class CreateHistoryView(APIView):
    def post(self, request):
        if request.user_ms.get("detail") != "unauthenticated":
            request.data.update({
                "employee_id": request.user_ms.get("id")
            })
            serializer = HistorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            publish("history_created", "history", serializer.data)
            publish("product_sold", "product", serializer.data.get("property_id"))
            return Response("Success")
        else:
            return Response("Authentication Required")
class CreateDemandView(APIView):
    def post(self, request):
        if request.user_ms.get("detail") != "unauthenticated":
            customer_path="customer/" + request.data.get("customer_id")
            customer=CustomerService.get(customer_path)
            print(customer.get("first_name"))
            request.data.update({

                "employee_id": request.user_ms.get("id"),
                "employee_first_name": request.user_ms.get("first_name"),
                "employee_last_name":request.user_ms.get("last_name"),
                "employee_email":request.user_ms.get("email"),
                "employee_is_employee":request.user_ms.get("is_employee"),
                "employee_phone_number":request.user_ms.get("phone_number"),
                "customer_id":customer.get("id"),
                "customer_first_name":customer.get("first_name"),
                "customer_last_name":customer.get("last_name"),
                "customer_phone_number":customer.get("phone_number"),

                
            })
            serializer = DemandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            print(serializer.data)
            publish("demand_created", "demand", serializer.data)
            return Response("Success")
        else:
            return Response("Authentication Required")
class ListProductView(APIView):
    def get(self, request):
        resp = ProductService.get("product_list")
        print(resp)
        return Response(resp)
class ListAdvertView(APIView):
    def get(self, request):
        resp = ProductService.get("advert_list")
        print(resp)
        return Response(resp)
class ListHistoryView(APIView):
    def get(self, request):
        resp = HistoryService.get("history_list")
        print(resp)
        return Response(resp)
