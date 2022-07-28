from django import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . views import *

urlpatterns = [
    path('api/shops',list_shops),
    path('api/shop/<int:id>',get_products),
]