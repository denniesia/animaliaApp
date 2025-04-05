from animaliaApp.animals.views import (index_view, dashboard_view, create_animal_view, delete_animal_view, \
    details_animal_view, edit_animal_view, create_category_view, create_owner_view, delete_owner_view,
                                       edit_owner_view, details_owner_view, rate_animal_view, top_rated_view)
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create-animal/', create_animal_view, name='create_animal'),
    path('create-owner/', create_owner_view, name='create_owner'),
    path('<int:pk>', include([
        path('delete-animal/', delete_animal_view, name='delete_animal'),
        path ('details-animal/', details_animal_view, name='details_animal'),
        path ('edit-animal/', edit_animal_view, name='edit_animal'),
    ])),
    path('create-category/', create_category_view, name='create_category'),
    path('<int:pk>', include([
        path('edit-owner/', edit_owner_view, name='edit_owner'),
        path('delete-owner/', delete_owner_view, name='delete_owner'),
        path('details-owner/', details_owner_view, name='details_owner'),
    ])),
    path('rate-animal/', rate_animal_view, name='rate_animal'),
    path('top-rated/', top_rated_view,  name='top_rated'),
]
