from django.urls import path, reverse_lazy
from . import views

app_name = 'autos'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('manufacturers/', views.manufacturers_page, name='manufacturers_page'),
    path('add_manufacturer/', views.manufacturer_add_form, name='add_manufacturer'),
    path('add_auto/', views.auto_add_form, name='add_auto'),
    path('<int:pk>/edit/', views.auto_edit_form, name='edit_auto'),
    path('<int:pk>/delete/', views.auto_delete, name='delete_auto'),
]
