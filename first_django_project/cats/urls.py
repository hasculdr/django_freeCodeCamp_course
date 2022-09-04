from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatsPage.as_view(), name='cats_page'),
    path('breeds/', views.BreedsPage.as_view(), name='breeds_page'),
    path('breed_create/', views.CreateBreed.as_view(), name='create_breed'),
    path('breed_update/<int:pk>/', views.UpdateBreed.as_view(), name='update_breed'),
    path('breed_delete/<int:pk>/', views.DeleteBreed.as_view(), name='delete_breed'),
    path('cat_create/', views.CreateCat.as_view(), name='create_cat'),
    path('cat_update/<int:pk>/', views.UpdateCat.as_view(), name='update_cat'),
    path('cat_delete/<int:pk>', views.DeleteCat.as_view(), name='delete_cat'),
]

