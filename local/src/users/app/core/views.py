import datetime

from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import User, UserToken
from .authentication import JWTAuthentication
from .serializers import UserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Passwords do not match!')
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        phone_number = request.data['phone_number']
        password = request.data['password']
        scope = request.data['scope']

        user = User.objects.filter(phone_number=phone_number).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect Password!')

        if user.is_employee and scope == 'admin':
            raise exceptions.AuthenticationFailed('Unauthorized')

        token = JWTAuthentication.generate_jwt(user.id, scope)

        UserToken.objects.create(
            user_id=user.id,
            token=token,
            created_at=datetime.datetime.utcnow(),
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=1)
        )

        return Response({
            'jwt': token
        })


class UserAPIView(APIView):
    def get(self, request, scope=''):
        token = request.COOKIES.get('jwt')
        if not token:
            raise exceptions.AuthenticationFailed('unauthenticated')

        payload = JWTAuthentication.get_payload(token)

        user = User.objects.get(pk=payload['user_id'])
        print(user)
        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')
        if not UserToken.objects.filter(user_id=user.id,
                                        token=token,
                                        expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
                                        ).exists():
            raise exceptions.AuthenticationFailed('unauthenticated')

        scope_admin_user_employee = user.is_employee and payload['scope'] != 'employee'
        scope_employee_user_admin = not user.is_employee and payload['scope'] != 'admin'
        scope_path_different = payload['scope'] != scope
        if scope_admin_user_employee or scope_employee_user_admin or scope_path_different:
            raise exceptions.AuthenticationFailed('unauthorized')
        return Response(UserSerializer(user).data)


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("CALISIYOR MU?")
        print(request.user)
        a = UserToken.objects.filter(user_id=request.user.id)
        a.delete()
        return Response({
            'message': 'success'
        })


# class ProfileInfoAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # def put(self, request, pk=None):
        # user = request.user
        # print("deneme")
        # serializer = UserSerializer(user, data=request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)


# class ProfilePasswordAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    # def put(self, request, pk=None):
        # user = request.user
        # data = request.data

        # if data['password'] != data['password_confirm']:
            # raise exceptions.APIException('Passwords do not match!')

        # user.set_password(data['password'])
        # user.save()
        # return Response(UserSerializer(user).data)


class UsersAPIView(APIView):
    def get(self, _, pk=None):
        if pk is None:
            return Response(UserSerializer(User.objects.all(), many=True).data)

        return Response(UserSerializer(User.objects.get(pk=pk)).data)
