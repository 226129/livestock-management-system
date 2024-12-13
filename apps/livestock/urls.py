from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('datos/', include("clinic.urls")),
    path('genealogia/', include("genealogy.urls")),
    path('gastos-ganancias/', include("costs.urls")),
]
