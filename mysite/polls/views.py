from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 1a2d4440 is the polls index.")
