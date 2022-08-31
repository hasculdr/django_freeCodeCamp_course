from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # для авторизации
from django.views import View
# from django.views.generic.edit import CreateView, UpdateView, DeleteView  # не использую здесь

from .models import Manufacturer, Auto
from .forms import MakerForm

"""
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
"""

class MainPage(LoginRequiredMixin, View):
    def get(self, request):
        autos = Auto.objects.all()
        manufacturers = Manufacturer.objects.all()
        context = {
            'autos': autos,
            'counter': len(manufacturers),
        }
        return render(request, 'autos/main_page.html', context)


"""
def manufacturers_page(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers}
    return render(request, 'autos/manufacturers_page.html', context)
"""


class MakersPage(LoginRequiredMixin, View):
    def get(self, request):
        makers = Manufacturer.objects.all()
        context = {'makers': makers}
        return render(request, 'autos/manufacturers_page.html', context)


"""
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
"""


class CreateMaker(LoginRequiredMixin, View):
    # переменные класса
    template = 'autos/add_or_edit_manufacturer.html'
    success_url = reverse_lazy('autos:main_page')

    def get(self, request):  # открытие страницы с пустой формой
        form = MakerForm()
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):  # отправка на сервер заполненной формы
        form = MakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template, context)


"""
def manufacturer_edit_form(request, pk):
    manufacturer = Manufacturer.objects.filter(pk=pk).values()
    dict_from_quiery_set = manufacturer[0]
    context = {
        'manufacturer_name': dict_from_quiery_set['name'],
        'manufacturer_id': dict_from_quiery_set['id'],
        'edit': True,
    }
    if request.method == 'POST':
        if request.POST.get('manufacturer'):
            post = Manufacturer()
            post.name = request.POST.get('manufacturer')
            post.id = dict_from_quiery_set['id']
            post.save()
            return redirect(reverse_lazy('autos:manufacturers_page'))
        elif request.POST.get('cancel'):
            return redirect(reverse_lazy('autos:manufacturers_page'))
    else:
        return render(request, 'autos/add_or_edit_manufacturer.html', context)

"""


class UpdateMaker(LoginRequiredMixin, View):
    model = Manufacturer  # переменная для работы с таблицей 'Manufacturer' (models.py)
    template = 'autos/add_or_edit_manufacturer.html'
    success_url = reverse_lazy('autos:main_page')

    def get(self, request, pk):
        maker = get_object_or_404(self.model, pk=pk)  # аналог запроса Manufacturer.objects.filter(pk=pk).values()
        form = MakerForm(instance=maker)  # объект с html-шаблоном на основе запроса выше
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request, pk):
        maker = get_object_or_404(self.model, pk=pk)
        form = MakerForm(request.POST, instance=maker)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template, context)


"""
def manufacturer_delete_form(request, pk):
    manufacturer = Manufacturer.objects.filter(pk=pk).values()
    context = {'manufacturer': manufacturer[0]}
    if request.method == 'POST':
        if request.POST.get('delete'):
            Manufacturer.objects.filter(pk=pk).delete()
            return redirect(reverse_lazy('autos:manufacturers_page'))
        elif request.POST.get('cancel'):
            return redirect(reverse_lazy('autos:manufacturers_page'))
    else:
        return render(request, 'autos/delete_manufacturer.html', context)
"""


class DeleteMaker(LoginRequiredMixin, View):
    model = Manufacturer
    template = 'autos/delete_manufacturer.html'
    success_url = reverse_lazy('autos:main_page')

    def get(self, request, pk):
        maker = get_object_or_404(self.model, pk=pk)
        context = {'maker': maker}
        return render(request, self.template, context)

    def post(self, request, pk):
        maker = get_object_or_404(self.model, pk=pk)
        maker.delete()
        return redirect(self.success_url)


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
