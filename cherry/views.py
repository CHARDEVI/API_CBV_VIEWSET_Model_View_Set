from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from cherry.views import *
from cherry.serializers import *




class ProductMVS(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer























