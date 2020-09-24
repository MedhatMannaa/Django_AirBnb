  
from django.urls import path
from units.views import all_units , single_unit


urlpatterns = [
    path('', all_units),
    path('<int:id>', single_unit)
]