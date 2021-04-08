from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, AccessToken, ChangePasswordSerializer, ChangeProfileSerializer, UserSerializer, UpdateUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login,logout
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser
# from django.contrib.auth.
# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            response={
                "username": user.username,
                'status_code':201,
            }
            return Response(response, status=201)
        return Response(serializer.errors, status=200)

class LoginView(APIView):
    permission_classes=(AllowAny,)
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data['user']
        login(request, user)
        access=AccessToken.for_user(user)
        respone={
            "id":user.id,
            "username":user.username,
            "superuser":user.is_superuser,
            "admin":user.is_staff,
            "status_code": 200,
            "token": str(access)
            
        }

        return Response(respone, status=200)


class LogoutView(APIView):
    permission_classes=(AllowAny,)
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CheckToken(APIView):
    def get(self, request):
        access=request.data['access']
        if AccessToken(access).check_blacklist():
            return Response({"token":"token in blacklisted", "status_code": 403}, status= 403)
        return Response({"token":access, "status_code": 200}, status=200)

class ChangePasswordView(APIView):
    def put(self, request):
        password=request.data['password']
        username=request.data['username']
        user=User.objects.get(username=username)
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(password)
            user.save()
            response={
                'username':user.username,
                'password':user.password,
                'status_code':200
            }
            return Response(response, status=200)
        return Response(serializer.errors, status=200)

class ChangeProfileView(APIView):
    def get(self, request, username):
        # username=request.data['username']
        user=User.objects.get(username=username)  
        serializer=ChangeProfileSerializer(user)
        if serializer:
            response={
                "data":serializer.data,
                "status_code": 200
            }
            return Response(response, status=200)
        return Response({"detai":"error", "status_code":400}, status=200)
    def put(self, request, username):
        # username=request.data['username']
        user=User.objects.get(username=username)
        serializer=ChangeProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                "user":serializer.data,
                "status_code": 200
            }
            return Response(response, status=200)
        return Response(serializer.errors, status=200)

class UserView(APIView):
    # permission_classes=(IsSuperUser,)
    def get(self, request):
        user=User.objects.all()
        serializer = UserSerializer(user, many=True)
        response={
            'data':serializer.data,
            'status_code':status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)

class UpdateUserView(APIView):
    # permission_classes=(IsSuperUser,)
    def get(self, request, username):
        # username=request.data['username']
        user=User.objects.get(username=username)  
        serializer=UpdateUserSerializer(user)
        if serializer:
            response={
                "data":serializer.data,
                "status_code": 200
            }
            return Response(response, status=200)
        return Response({"detai":"error", "status_code":400}, status=200)

    def put(self, request, username):
        # username=request.data['username']
        user=User.objects.get(username=username)
        serializer=UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response={
                "data":serializer.data,
                "status_code": 200
            }
            return Response(response, status=200)
        return Response(serializer.errors, status=400)