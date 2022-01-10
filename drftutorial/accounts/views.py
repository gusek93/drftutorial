from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class UserCreate(generics.CreateAPIView):
    qs = User.objects.all()
    serializer_class = UserSerializer
    
    
    # def post(self, request):
    #     return Response(status=status.HTTP_200_OK)