from django.urls import path
from . import views

urlpatterns=[
    path("",views.list_places,name="places"),
    path("addplaces/<int:id>/",views.add_place,name="addplace"),
    path("myplaces/",views.my_places, name="myplaces"),
    path("delete/<int:id>/",views.delete_myplace,name="deleteplace"),
    path("edit/<int:id>",views.edit_myplace,name="editplace"),
]
