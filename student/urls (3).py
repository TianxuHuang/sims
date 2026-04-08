from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('list/', views.list_student, name='list_student'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
