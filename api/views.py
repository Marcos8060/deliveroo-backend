from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny



# user registration view
class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class Products(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer

