from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('list/', views.list_course, name='list_course'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('delete/<int:pk>/', views.delete_course, name='delete_course'),
]
