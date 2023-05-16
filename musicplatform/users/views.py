from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UsersSerializer
from rest_framework.permissions import IsAdminUser
# Create your views here.
class Users(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UsersSerializer(user,many=False)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message':'DoesNotExist'},status=status.HTTP_404_NOT_FOUND)    
    def put(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UsersSerializer(instance=user,data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message':'DoesNotExist'},status=status.HTTP_404_NOT_FOUND)    
    def patch(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UsersSerializer(instance=user,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message':'DoesNotExist'},status=status.HTTP_404_NOT_FOUND)