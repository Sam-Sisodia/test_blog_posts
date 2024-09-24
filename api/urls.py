
from django.urls import path
from .  import views 
from rest_framework.routers import DefaultRouter

routers =  DefaultRouter()

routers.register("rest-data/", views.RestoAPI ,basename="rest-data" )

urlpatterns = [
    
    
]+routers.urls
