from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('delete/<str:id>/', delete, name="delete"),
    path('ajax-data/', ajax_data, name="ajax_data"),
]