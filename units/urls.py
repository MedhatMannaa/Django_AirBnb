  
from django.urls import path
from units.views import all_units , single_unit , new_unit , edit_unit , PostList , PostDetail , PostUpdate

app_name='units'

urlpatterns = [
    path('', all_units, name='unit_list'),
    path('new', new_unit, name='new_unit'),
    path('<int:id>', single_unit, name='unit_detail'),
    path('<int:id>/edit', edit_unit, name='edit_unit'),

    path('cbv', PostList.as_view()),
    path('cbv/<int:pk>', PostDetail.as_view() , name='cbv_detail'),
    path('cbv/<int:pk>/edit', PostUpdate.as_view()),
]