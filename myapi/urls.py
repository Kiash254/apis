from django import views
from django.urls import include, path
from .views import hero
from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'hero',HeroViewSet)

app_name="myapi"


urlpatterns = [
    # path("",home,name="home"),
    # path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path("",hero,name="hero"),
    # path("depart/",depart,name="depart")
]
