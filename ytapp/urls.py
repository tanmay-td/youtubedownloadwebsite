from django.urls import path,include
from .views import index,youtubevideo

urlpatterns = [
    path('',youtubevideo,name='index')
]