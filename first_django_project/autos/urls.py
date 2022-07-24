from django.urls import path, reverse_lazy
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('manufacturers/', views.manufacturers_page, name='manufacturers_page'),
    path('add_auto/', views.auto_form, name='add_auto'),
    path('add_manufacturer/', views.manufacturer_form, name='add_manufacturer'),
]