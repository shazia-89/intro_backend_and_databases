from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todos_list, name='todos_list'),  # The list of todos
    path('<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
]