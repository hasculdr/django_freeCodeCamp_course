from django.urls import path
from . import views

appname = 'hello'
urlpatterns = [
    path('', views.diy, name='hello'),
]
