from django.shortcuts import redirect , render
from .models import Unit
from .forms import UnitForm
from django.urls import reverse
from django.views.generic import ListView , DetailView , UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Class Bassed Views
class PostList(ListView):
    model = Unit

class PostDetail(DetailView):
    model = Unit

class PostUpdate(UpdateView):
    model = Unit 
    fields = '__all__'
    success_url = '/units/cbv'

# Function Bassed Views
#@login_required
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
            return redirect(reverse('unit:unit_list'))

    else: # show unit
        form = UnitForm()
    return render(request,'unit/new.html',{'form':form})  

def edit_unit(request,id):
    ## Logic
    single_unit = Unit.objects.get(id=id)
    if request.method=='POST': # add new unit
        form = UnitForm(request.POST or None , request.FILES , instance=single_unit )
        if form.is_valid():
            form.save()
            return redirect(reverse('unit:edit_unit'))

    else: # show unit
        form = UnitForm(instance=single_unit)
    return render(request,'unit/new.html',{'form':form})  