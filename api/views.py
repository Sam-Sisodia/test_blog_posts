from django.shortcuts import render
from . models import *

# Create your views here.

from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet


class Restoserializer(serializers.ModelSerializer):
    class Meta:
        model= Bugger
        fields = "__all__"




class RestoAPI(ModelViewSet):
    serializer_class = Restoserializer
    queryset = Bugger.objects.all()
    