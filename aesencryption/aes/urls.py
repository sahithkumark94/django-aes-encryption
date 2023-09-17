from django.urls import path
from aes.views import *

urlpatterns = [
    path('encrypt', views.encryt),
    path('decrypt', views.decrypt),

    path('encryptUrlParam', views.encrytUrlParam),
    path('decryptUrlParam', views.decryptUrlParam),
    
    
]