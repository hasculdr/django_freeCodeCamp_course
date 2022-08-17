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
        'edit': False,
    }
    return render(request, 'autos/main_page.html', context)


def manufacturers_page(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers}
    return render(request, 'autos/manufacturers_page.html', context)


def auto_add_form(request):
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
        # else - нет проверки введенных данных
        elif request.POST.get('cancel'):
            return redirect(reverse_lazy('autos:main_page'))
    elif request.method == 'GET':
        return render(request, 'autos/add_or_edit_auto.html', context)


def auto_edit_form(request, pk):
    auto = Auto.objects.filter(pk=pk).values()
    chosen_man = Manufacturer.objects.filter(pk=auto[0]['auto_id']).values()
    manufacturers = Manufacturer.objects.all()
    context = {
        'auto': auto[0],
        'manufacturers': manufacturers,
        'chosen_man': chosen_man[0],
        'edit': True,
    }
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
        elif request.POST.get('cancel'):
            return redirect(reverse_lazy('autos:main_page'))
    elif request.method == 'GET':
        return render(request, 'autos/add_or_edit_auto.html', context)


def auto_delete(request, pk):
    auto = Auto.objects.filter(pk=pk).values() # это объект <QuerySet [{'id': 8, 'nickname': 'Ведро', 'mileage': 20, 'comments': 'с болтами', 'auto_id': 10}]>
    context = {'auto': auto[0]}
    if request.method == 'POST': # нажатие кнопок в форме на странице подтверждения
        if request.POST.get('delete'):
            Auto.objects.filter(pk=pk).delete()
            return  redirect(reverse_lazy('autos:main_page'))
        elif request.POST.get('cancel'):
            return  redirect(reverse_lazy('autos:main_page'))
    else: # нажатие на ссылку "удалить", рендер страницы с подтверждением
        return render(request, 'autos/delete_record.html', context)


def manufacturer_add_form(request):
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
