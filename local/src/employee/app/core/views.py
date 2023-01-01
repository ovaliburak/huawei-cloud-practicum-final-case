import json
import time
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from core.services import UserService
from core.services import CustomerService
from core.services import ProductService
from core.services import HistoryService
from core.services import DemandService
from core.producer import publish
from core.serializers import CustomerEmployeeSerializer
from core.serializers import ProductEmployeeSerializer
from core.serializers import AdvertEmployeeSerializer
from core.serializers import HistorySerializer
from core.serializers import DemandSerializer
from core.match import Match
from core.notification import send_message_to_customer, send_message_to_employee
from django.http import QueryDict

class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        data["is_employee"] = True
        if not request.data.get("password") or not request.data.get("password_confirm"):
            raise exceptions.APIException("Password or Password Confirm must set.")
        else:
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
            return Response(CustomerService.post("customer_create/", data=serializer.data))
        else:
            return Response("Authentication Required")

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
            return Response(ProductService.post("product_create/", data=serializer.data))
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
            return Response(ProductService.post("advert_create/", data=serializer.data))
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
            HistoryService.post("history_create/", data=serializer.data)
            ProductService.post("product_sold/", data=serializer.data)
            return Response("Success")
        else:
            return Response("Authentication Required")
class CreateDemandView(APIView):
    def post(self, request):
        if request.user_ms.get("detail") != "unauthenticated":
            customer_path="customer/" + request.data.get("customer_id")
            customer=CustomerService.get(customer_path)
            request_raw_data=request.data
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
            request_raw_data["customer_first_name"]=customer.get("first_name")
            request_raw_data["customer_last_name"]=customer.get("last_name")
            request_raw_data["customer_phone_number"]=customer.get("phone_number")
            request_raw_data["employee_first_name"]=request.user_ms.get("first_name")
            request_raw_data["employee_last_name"]=request.user_ms.get("last_name")
            request_raw_data["employee_phone_number"]=request.user_ms.get("phone_number")
       
            serializer = DemandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            DemandService.post("demand_create/", data=serializer.data)
            # publish("demand_created", "demand", serializer.data)
            products=ProductService.get('product_list')
            match_rate = Match.product_compare(products, request_raw_data)
            print(match_rate)
            for i in match_rate:
                send_message_to_customer(i)
                send_message_to_employee(i) 
            return Response("Success")
        else:
            return Response("Authentication Required")
class ListCustomerView(APIView):
    def get(self, request):
        resp = CustomerService.get("customer_list")
        return Response(resp)
    
class RetrieveCustomerView(APIView):
    def get(self, request, pk):
        resp = CustomerService.get(f"customer/{pk}/")
        return Response(resp)
class ListProductView(APIView):
    def get(self, request):
        resp = ProductService.get("product_list")
        return Response(resp)
    
class RetrieveProductView(APIView):
    def get(self, request, pk):
        resp = ProductService.get(f"product/{pk}/")
        return Response(resp)
class ListAdvertView(APIView):
    def get(self, request):
        resp = ProductService.get("advert_list")
        return Response(resp)
class RetrieveAdvertView(APIView):
    def get(self, request, pk):
        resp = ProductService.get(f"advert/{pk}/")
        return Response(resp)
class ListHistoryView(APIView):
    def get(self, request):
        resp = HistoryService.get("history_list")
        return Response(resp)
class ListDemandView(APIView):
    def get(self, request):
        resp = DemandService.get("demand_list")
        return Response(resp)
class RetrieveDemandView(APIView):
    def get(self, request, pk):
        resp = DemandService.get(f"demand/{pk}/")
        return Response(resp)