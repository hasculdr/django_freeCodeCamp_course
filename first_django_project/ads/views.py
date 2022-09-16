from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from ads.models import Ad
from ads.forms import CreateForm
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/list.html'
    # By convention:
    # template_name = "ads/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/detail.html'

class AdCreateView(LoginRequiredMixin, View):
    template_name='ads/form.html'
    success_url=reverse_lazy('ads:all')

    def get(self, request):
        form = CreateForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)
        if form.is_valid():
            # Add owner to the model before saving
            pic = form.save(commit=False)
            pic.owner = self.request.user
            pic.save()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)


class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/delete.html'


def stream_file(request, pk):
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
