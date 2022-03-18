from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Heroserial
from .models import Hero ,Department

# class HeroViewSet(viewsets.ModelViewSet):
#     queryset=Hero.objects.all().order_by('name')
#     serialize_class=Heroserial

# def hero(request):
#     hero=Hero.objects.all()
#     context={
#         "hero":hero
#     }
#     return render(request,"hero.html",context)
# def depart(request):
#     depart=Department.objects.all()
#     context={
#         "depart":depart
#     }
#     return render(request,"depart.html",context)

#get and post

@api_view(['GET','POST'])
def hero(request):
    if request.method == 'GET':
        heros = Hero.objects.all()
        serializer = Heroserial(heros, many=True)
        return Response(serializer.data)