from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cat, Breed
from .forms import CatForm, BreedForm


class CatsPage(LoginRequiredMixin, View):
    def get(self, request):
        cats = Cat.objects.all()
        breeds_counter = Breed.objects.all().count()
        context = {
            'cats': cats,
            'breeds_counter': breeds_counter
        }
        return render(request, 'cats/cats_page.html', context)

class BreedsPage(LoginRequiredMixin, View):
    def get(self, request):
        breeds = Breed.objects.all()
        context = {'breeds': breeds}
        return render(request, 'cats/breeds_page.html', context)

class CreateBreed(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cats_page')

    def get(self, request):
        form = BreedForm()
        context = {
            'form': form,
            'header': 'Добавление породы',
            'button': 'Добавить',
            }
        return render(request, self.template, context)

    def post(self, request):
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
                'header': 'Добавление породы',
                'button': 'Добавить',
            }
            return render (request, self.template, context)

class UpdateBreed(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:cats_page')

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        context = {
            'form': form,
            'header': 'Обновление породы',
            'button': 'Обновить',
            }
        return render(request, self.template, context)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
                'header': 'Обновление породы',
                'button': 'Обновить',
            }
            return render(request, self.template, context)

class DeleteBreed(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/breed_delete.html'
    success_url = reverse_lazy('cats:cats_page')

    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        context = {'breed': breed}
        return render(request, self.template, context)

    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)

class CreateCat(LoginRequiredMixin, View):
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cats_page')

    def get(self, request):
        form = CatForm
        context = {
            'form': form,
            'header': 'Добавление кошарика',
            'button': 'Добавить',
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
                'header': 'Добавление кошарика',
                'button': 'Добавить',
            }
            return render(request, self.template, context)

class UpdateCat(LoginRequiredMixin, View):
    model = Cat
    template = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:cats_page')

    def get(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        form = CatForm(instance=cat)
        context = {
            'form': form,
            'header': 'Обновление кошарика',
            'button': 'Обновить',
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {
                'form': form,
                'header': 'Обновление кошарика',
                'button': 'Обновить',
            }
            return render(request, self.template, context)

class DeleteCat(LoginRequiredMixin, View):
    model = Cat
    template = 'cats/cat_delete.html'
    success_url = reverse_lazy('cats:cats_page')

    def get(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        context = {'cat': cat}
        return render(request, self.template, context)

    def post(self, request, pk):
        cat = get_object_or_404(self.model, pk=pk)
        cat.delete()
        return redirect(self.success_url)

