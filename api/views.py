from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
class Products(generics.ListCreatAPIView):
    queryset = Product.ojects.all()
    serializer_class = ProductSerializer

