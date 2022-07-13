from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('manufacturers/', views.manufacturers_page, name='manufacturers_page'),
    path('add_auto/', views.add_auto, name='add_auto'),
    path('add_manufacturer/', views.add_manufacturer, name='add_manufacturer'),
]