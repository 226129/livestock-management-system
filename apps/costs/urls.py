from django.urls import path
from .views import *

urlpatterns = [
    path('', costs, name='costos'),
]
