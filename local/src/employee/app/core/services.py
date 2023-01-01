import os, requests


class UserService:
    # endpoint = os.getenv('USERS_MS') + '/api/'
    endpoint = "http://0.0.0.0:8000" + '/api/'

    @staticmethod
    def get(path, **kwargs):
        headers = kwargs.get('headers', [])
        return requests.get(UserService.endpoint + path, headers=headers).json()

    @staticmethod
    def post(path, **kwargs):
        headers = kwargs.get('headers', [])
        data = kwargs.get('data', [])
        return requests.post(UserService.endpoint + path, data=data, headers=headers).json()

    @staticmethod
    def put(path, **kwargs):
        headers = kwargs.get('headers', [])
        data = kwargs.get('data', [])
        return requests.put(UserService.endpoint + path, data=data, headers=headers).json()

class CustomerService:
    endpoint="http://127.0.0.1:8002" + "/api/"

    @staticmethod
    def get(path):
        return requests.get(CustomerService.endpoint + path).json()
    
    @staticmethod
    def post(path, **kwargs):
        data = kwargs.get('data', [])
        return requests.post(CustomerService.endpoint + path, data=data).json()

class ProductService:
    endpoint="http://127.0.0.1:8003" + "/api/"

    @staticmethod
    def get(path):
        return requests.get(ProductService.endpoint + path).json()
    
    @staticmethod
    def post(path, **kwargs):
        data = kwargs.get('data', [])
        return requests.post(ProductService.endpoint + path, data=data).json()

class HistoryService:
    endpoint="http://127.0.0.1:8004" + "/api/"

    @staticmethod
    def get(path):
        return requests.get(HistoryService.endpoint + path).json()
    
    @staticmethod
    def post(path, **kwargs):
        data = kwargs.get('data', [])
        return requests.post(HistoryService.endpoint + path, data=data).json()
    

class DemandService:
    endpoint="http://127.0.0.1:8005" + "/api/"

    @staticmethod
    def get(path):
        return requests.get(DemandService.endpoint + path).json()
    
    @staticmethod
    def post(path, **kwargs):
        data = kwargs.get('data', [])
        return requests.post(DemandService.endpoint + path, data=data).json()

