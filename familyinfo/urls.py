from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:did>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('edit/<int:eid>/', views.edit, name='edit'),
]