from django.shortcuts import render
from .models import Unit
from .forms import UnitForm

# Create your views here.

def all_units(request):
    ## Logic
    all_units = Unit.objects.all()
    return render(request,'unit/all_units.html' ,{'units':all_units})

def single_unit(request,id):
    ## Logic
    single_unit = Unit.objects.get(id=id)
    return render(request,'unit/single_unit.html' ,{'unit':single_unit})   

def new_unit(request):
    ## Logic
    if request.method=='POST': # add new unit
        form = UnitForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()

    else: # show unit
        form = UnitForm()
    return render(request,'unit/new.html',{'form':form})  
