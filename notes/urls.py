
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]