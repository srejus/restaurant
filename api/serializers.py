from rest_framework import serializers
from home.models import *
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('__all__')

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('__all__')


