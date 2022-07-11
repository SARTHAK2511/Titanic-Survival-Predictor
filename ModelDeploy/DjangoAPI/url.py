
from pkgutil import ImpImporter
from django.contrib import admin
from django.urls import path,include

from DjangoAPI import views

urlpatterns = [
path('',views.home,name='home'),    
path('about',views.about,name='about'),
path('result',views.result,name='result'),
path('about',views.about,name='about')
]
