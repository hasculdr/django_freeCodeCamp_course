from django.shortcuts import render
from .models import Peeps, Names, Patronymics
from .forms import PeepsForm, NamesForm, PatronymicsForm

def index(request):
    peeps = Peeps.objects.all()
    return render(request, 'test_phonebook/index.html', {'key': peeps})

def add(request):
    message = ''
    if request.method == 'POST':
        peep = PeepsForm(request.POST)
        name = NamesForm(request.POST)
        patronymic = PatronymicsForm(request.POST)
        if peep.is_valid() and name.is_valid() and patronymic.is_valid():
            peep.save()
            name.save()
            patronymic.save()
            message = 'Запись добавлена'
        else:
            message = 'Ошибка ввода'

    peep = PeepsForm()
    name = NamesForm()
    patronymic = PatronymicsForm()
    context = {
        'peeps': peep,
        'names': name,
        'patronymics': patronymic,
        'message': message,
    }
    return render(request, 'test_phonebook/add.html', context)

def get(request):
    if request.method == 'POST':
        peep = PeepsForm(request.POST)
        name = NamesForm(request.POST)
        patronymic = PatronymicsForm(request.POST)