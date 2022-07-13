from django.shortcuts import render, get_object_or_404
from .models import Manufacturer, Auto


def main_page(request):
    autos = Auto.objects.all()
    manufacturers = Manufacturer.objects.all()
    context = {
        'autos': autos,
        'manufacturers': manufacturers,
        'counter': len(manufacturers),
    }
    return render(request, 'autos/main_page.html', context)

def manufacturers_page(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers,}
    return render(request, 'autos/manufacturers_page.html', context)

def add_auto(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers,}
    return render(request, 'autos/add_auto.html', context)

def add_manufacturer(request):
    return render(request, 'autos/add_manufacturer.html')