
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [

    path('',views.index),
    path('search/', views.search_quotes, name='search'),
]
