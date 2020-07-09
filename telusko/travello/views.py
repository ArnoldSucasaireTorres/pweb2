from django.shortcuts import render
from .models import Destination
from .forms import DestinosForm
# Create your views here.


def index(request):
    
    dests = Destination.objects.all()

    return render(request,"index.html", {'dests': dests})

def Destinos(request):
    form = DestinosForm()
    context = {
        'form': form,
    }
    return render(request, '')