from operator import imod
from pyexpat import model
from rest_framework import serializers
from rx import alias
from .models import Hero

class Heroserial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        fields=('name','alias')