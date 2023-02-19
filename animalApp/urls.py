from django.urls import path
from .views import *

urlpatterns = [
    # path('test', siting_view, name="breed-list"),
    path('', home.as_view(), name="home"),
    path('delete/<str:id>/', delete, name="delete"),
    # path('index', index, name="index-1"),
    # path('tt', sittings_list, name='sittings_list'),
    # path('new', new_siting, name='new_siting'),
    # path('ajax/get_breeds/int:animal_id/', ajax_get_breeds, name='ajax_get_breeds'),
]