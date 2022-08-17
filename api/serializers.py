from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.models import User



class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)
    # profiles = serializers.PrimaryKeyRelatedField(many=True, queryset=Profile.objects.all())
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'