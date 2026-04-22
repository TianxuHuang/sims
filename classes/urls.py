from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('list/', views.list_class, name='list_class'),
    path('add/', views.add_class, name='add_class'),
    path('edit/<int:pk>/', views.edit_class, name='edit_class'),
    path('delete/<int:pk>/', views.delete_class, name='delete_class'),
]
