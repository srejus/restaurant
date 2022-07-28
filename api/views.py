from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Q 

from . serializers import *
from home.models import *

@api_view(['GET'])
def list_shops(request):
    shps = Shop.objects.all()
    serializers = ShopSerializer(shps,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_products(request,id):
    prodts = Menu.objects.filter(shop__id=id)
    serializer = MenuSerializer(prodts,many=True)
    return Response(serializer.data)
   
