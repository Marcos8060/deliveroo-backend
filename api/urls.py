from django.urls import path
from .views import *

urlpatterns = [
    path('products/', Products.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view())
]