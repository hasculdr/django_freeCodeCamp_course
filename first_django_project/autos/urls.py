from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [
    # path('', views.main_page, name='main_page'),
    # path('manufacturers/', views.manufacturers_page, name='manufacturers_page'),
    # path('add_manufacturer/', views.manufacturer_add_form, name='add_manufacturer'),
    # path('<int:pk>/edit_manufacturer/', views.manufacturer_edit_form, name='edit_manufacturer'),
    # path('<int:pk>/delete_manufacturer/', views.manufacturer_delete_form, name='delete_manufacturer'),
    path('', views.MainPage.as_view(), name='main_page'),
    path('makers/', views.MakersPage.as_view(), name='makers_page'),
    path('add_maker/', views.CreateMaker.as_view(), name='add_maker'),
    path('edit_maker/<int:pk>/', views.UpdateMaker.as_view(), name='edit_maker'),
    path('delete_maker/<int:pk>/', views.DeleteMaker.as_view(), name='delete_maker'),
    path('add_auto/', views.auto_add_form, name='add_auto'),
    path('<int:pk>/edit_auto/', views.auto_edit_form, name='edit_auto'),
    path('<int:pk>/delete_auto/', views.auto_delete, name='delete_auto'),
]
