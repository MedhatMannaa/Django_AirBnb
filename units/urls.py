  
from django.urls import path
from units.views import all_units , single_unit

app_name='units'

urlpatterns = [
    path('', all_units),
    path('<int:id>', single_unit, name='unit_detail')
]