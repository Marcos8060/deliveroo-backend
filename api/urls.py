from django.urls import path
from .views import *

urlpatterns = [
    path('products/', Products.as_view())
]