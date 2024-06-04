import datetime
import jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.models import User

from .serializers import UserSerializer

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        ser = UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)



class LoginView(APIView):

    def post(self, request):
        user_name = request.data['username']
        password = request.data['password']

        try:
            user_obj: User = User.objects.get(username=user_name)
        except:
            raise AuthenticationFailed('User not found!')

        if not user_obj.check_password(password):
            raise AuthenticationFailed('password is not correct')

        playload = {
            "id": user_obj.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(playload, 'dana', algorithm='HS256')

        reponse = Response()

        reponse.set_cookie(key='jwt', value=token, httponly=True)

        reponse.data = {'token': token}

        return reponse


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('token is not valid')

        try:
            payload = jwt.decode(token, 'dana', algorithms=["HS256"])
        except:
            raise AuthenticationFailed('token is not valid')

        try:
            user = User.objects.get(id=payload['id'])
        except:
            raise AuthenticationFailed('user not found!')

        ser = UserSerializer(user)

        return Response(ser.data)


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logout'
        }
        return response

