from django.shortcuts import render,redirect
from .models import Place,AddPlace
from .forms import EditplaceForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def list_places(request):
    places=Place.objects.all()
    return render(request,"allplaces.html",{"places":places})

@login_required
def my_places(request):
    try:
        myplaces=AddPlace.objects.filter(usr=request.user)
    except:
        myplaces=None
    return render(request,"myplaces.html",{"myplaces":myplaces})
@login_required
def add_place(request,**kwargs):
    id=kwargs["id"]
    place=Place.objects.get(pk=id)
    AddPlace.objects.create(
        name=place.name,
        addr=place.addr,
        open_time=place.open_time,
        close_time=place.close_time,
        usr=request.user)
    return redirect(my_places)
@login_required
def edit_myplace(request,**kwargs):
    id=kwargs["id"]
    form=EditplaceForm(instance=AddPlace.objects.get(pk=id))
    if request.method=="POST":
        form=EditplaceForm(instance=AddPlace.objects.get(pk=id),data=request.POST)
        if form.is_valid:
            form.save()
            return redirect(my_places)
    return render(request,"editplaces.html",{"form":form,"id":id})
@login_required
def delete_myplace(request,**kwargs):
    id=kwargs["id"]
    AddPlace.objects.get(pk=id).delete()
    return redirect(my_places)
