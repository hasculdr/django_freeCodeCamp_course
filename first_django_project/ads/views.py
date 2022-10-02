from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ads.models import Ad, Comment, Fav
from ads.forms import CreateForm, CommentForm
from ads.owner import OwnerListView, OwnerDetailView
from ads.owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from django.db.models import Q

# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/list.html'
    # By convention:
    # template_name = "ads/ad_list.html"

    def get(self, request):
        search_val = request.GET.get('search', False)
        if search_val:
            # поиск только по заголовкам
            # objects = Ad.objects.filter(title__contains=search_val)
            # поиск по нескольким полям
            # __icontains для регистрозависимого поиска,
            # только по Char/TextField
            query = Q(title__icontains=search_val)
            query.add(Q(text__icontains=search_val), Q.OR)
            ad_list = Ad.objects.filter(query)
        else:
            ad_list = Ad.objects.all()
        for elem in ad_list:
            elem.natural_updated = naturaltime(elem.updated_at)
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_ads.values('id')
            # favorites = [2, 4, ...] using list comprehension
            favorites = [row['id'] for row in rows]
        ctx = {
            'ad_list': ad_list,
            'favorites': favorites,
            'search': search_val
        }
        return render(request, self.template_name, ctx)


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/detail.html'

    def get(self, request, pk):
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = {
            'ad': x,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, self.template_name, context)


class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/form.html'
    success_url = reverse_lazy('ads:all')

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


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'],
                          owner=request.user, ad=f)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])


@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Add PK", pk)
        t = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Delete PK", pk)
        t = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, ad=t).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()
