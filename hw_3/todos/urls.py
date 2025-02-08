from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # List all Todos
    path('<int:id>/', views.todo_detail, name='todo_detail'),  # View a single Todo
    path('add/', views.add_todo, name='add_todo'),  # Add a new Todo
    path('<int:id>/delete/', views.delete_todo, name='delete_todo'),  # Delete a Todo
]
