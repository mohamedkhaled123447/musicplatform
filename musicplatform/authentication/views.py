from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .serializers import RegistrationSerializer
import django.contrib.auth.password_validation as validators
from knox.auth import AuthToken
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# Create your views here.
class Register(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            validators.validate_password(request.data['password'])
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        if request.data['password'] == request.data['password1']:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'passwords do not match'},status=status.HTTP_400_BAD_REQUEST)    

class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        if user:
            _,token = AuthToken.objects.create(user)
            login(request,user)
            return Response({'Token':token,'user':{'id':user.id,'username':user.username,'email':user.email,'bio':user.bio}},status=status.HTTP_200_OK)
        else:
            return Response({'error':'invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
class Logout(APIView):
    def post(self,request):
        user=request.user
        logout(request)
        return Response({'message':f'{user}logged out successfully'},status=status.HTTP_200_OK)            