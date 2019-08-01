from django.urls import path

from . import views

urlpatterns = [
    path('/ufc', views.index, name='index'),
]