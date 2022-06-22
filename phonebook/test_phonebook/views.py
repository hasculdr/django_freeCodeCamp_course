from django.shortcuts import render
from .models import Peeps, Names, Patronymics
from .forms import PeepsForm, NamesForm, PatronymicsForm

def index(request):
    peeps = Peeps.objects.all()
    return render(request, 'test_phonebook/index.html', {'key': peeps})

def add(request):
    peep = PeepsForm()
    name = NamesForm()
    patronymic = PatronymicsForm()
    context = {
        'peeps': peep,
        'names': name,
        'patronymics': patronymic
    }
    return render(request, 'test_phonebook/add.html', context)
