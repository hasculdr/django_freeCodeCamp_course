from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
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
    context = {'manufacturers': manufacturers}
    return render(request, 'autos/manufacturers_page.html', context)


def auto_form(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers}
    if request.method == 'POST':
        if request.POST.get('nickname') and request.POST.get('mileage') and request.POST.get('comment') and (request.POST.get('manufacturer') != '-----'):
            post = Auto()
            post.nickname = request.POST.get('nickname')
            post.mileage = request.POST.get('mileage')
            post.comments = request.POST.get('comment')
            '''
            Достаем id значения в поле <select>: Manufacturer.objects.filter(name=request.POST.get('manufacturer')).values()[0]['id'],
            где request.POST.get('manufacturer') - выбранное значение поля <select>,
            Manufacturer.objects.filter(фильтр).values() - запрос всех значений из таблицы Manufacturers, ответ - объект QuierySet[{}]
            [0]['id'] для <QuerySet [{'id': 1, 'name': 'BMW'}]> вернет 1
            '''
            manufacturer_id = Manufacturer.objects.filter(name=request.POST.get('manufacturer')).values()[0]['id']
            post.auto_id = manufacturer_id
            post.save()
            return redirect(reverse_lazy('autos:main_page'))
        elif request.POST.get('cancel'):
            return redirect(reverse_lazy('autos:main_page'))
    elif request.method == 'GET':
        return render(request, 'autos/add_auto.html', context)


def manufacturer_form(request):
    if request.method == 'POST':  # нажатие на кнопку submit
        if request.POST.get('manufacturer'):  # проверка содержимого в поле "Производитель" html-формы; параметр 'manufacturer' - значение параметра 'name' соответствующего поля ввода формы
            post = Manufacturer()  # переменная для работы с таблицей 'Manufacturer' (models.py)
            post.name = request.POST.get('manufacturer')  # присваиваем переменной таблицы значение, полученное из html-формы
            post.save()  # сохраняем запись в таблице
            return redirect(reverse_lazy('autos:main_page'))
        elif request.POST.get('cancel'):
            return redirect(reverse_lazy('autos:main_page'))
    else:
        return render(request, 'autos/add_manufacturer.html')
