from django.urls import path
#Importamos las funciones necesarias para usarlas
from .views import listTask, createTask, deleteTask



urlpatterns = [
    path('', listTask),
    path('new/', createTask, name='createTask'),
    path('deleteTask/<int:idTask>/', deleteTask, name='deleteTask'),
]

