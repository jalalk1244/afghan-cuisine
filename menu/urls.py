from . import views
from django.urls import path

urlpatterns = [
    path('menu', views.DishesList.as_view(), name='menu'),
]
