import os, requests


class UserService:
    # endpoint = os.getenv('USERS_MS') + '/api/'
    endpoint = "http://127.0.0.1:8000" + '/api/'

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
