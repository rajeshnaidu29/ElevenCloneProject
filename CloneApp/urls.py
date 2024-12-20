from django.urls import path
from .views import *

app_name='CloneApp'

urlpatterns=[
    path('',main,name='main'),
    path('home/',home,name='home'),
    path('course/',course,name='course'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('request/',request,name='request'),
    path('signin/',signin,name='signin'),

]