from django.urls import path
from aes.views import *

urlpatterns = [
    path('encrypt', views.encryt),
    
]