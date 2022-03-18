from django.shortcuts import render
from html5lib import serialize
from .models import Hero
from rest_framework import viewsets
from .serializers import Heroserial
# Create your views here.
# def home(request):
#     hero=Hero.objects.all()
#     context={
#         "hero":hero
#     }
#     return render(request,"home.html",context)

class HeroViewSet(viewsets.ModelViewSet):
    queryset=Hero.objects.all().order_by('name')
    serialize_class=Heroserial