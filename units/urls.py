  
from django.urls import path
from units.views import all_units , single_unit , new_unit

app_name='units'

urlpatterns = [
    path('', all_units, name='unit_list'),
    path('new', new_unit, name='new_unit'),
    path('<int:id>', single_unit, name='unit_detail')
]