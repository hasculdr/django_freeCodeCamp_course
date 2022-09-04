from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatsPage.as_view(), name='cats_page'),
    path('breeds/', views.BreedsPage.as_view(), name='breeds_page'),
    path('create/breed/', views.CreateBreed.as_view(), name='create_breed'),
    path('update/breed/<int:pk>/', views.UpdateBreed.as_view(), name='update_breed'),
    path('delete/breed/<int:pk>/', views.DeleteBreed.as_view(), name='delete_breed'),
    path('create/cat/', views.CreateCat.as_view(), name='create_cat'),
    path('update/cat/<int:pk>/', views.UpdateCat.as_view(), name='update_cat'),
    path('delete/cat/<int:pk>', views.DeleteCat.as_view(), name='delete_cat'),
]

