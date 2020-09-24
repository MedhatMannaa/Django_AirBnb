from django.shortcuts import render
from .models import Unit

# Create your views here.

def all_units(request):
    ## Logic
    all_units = Post.objects.all()
    return render(request,'unit/all_units.html' ,{'units':all_units})

def single_unit(request,id):
    ## Logic
    single_unit = Post.objects.get(id=id)
    return render(request,'unit/single_unit.html' ,{'unit':single_unit})   