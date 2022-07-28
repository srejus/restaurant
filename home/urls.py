from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.Login,name='login'),
    path('signup',views.signup,name='signup'),
    path('shop/<int:id>',views.menu,name='menu'),
    path('restaurant/manage',views.rest_manage,name='rest_manage'),
    path('rest_menu/<int:id>',views.rest_menu,name='rest_menu'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('add_item/<int:id>',views.add_item,name='add_item'),
    path('delete_shop/<int:id>',views.delete_shop,name='delete_shop'),
    path('add_shop',views.add_shop,name='add_shop'),
]
