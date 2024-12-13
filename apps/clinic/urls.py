from django.urls import path
from .views import *

urlpatterns = [
    path('', datos, name='datos'),
]
