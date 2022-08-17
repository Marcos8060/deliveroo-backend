from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/',UsersList.as_view(),name='create_user'),
    path('products/', Products.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('cart/', CartItems.as_view()),


    # TOKEN
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # TOKEN BLACKLIST
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist'),
]