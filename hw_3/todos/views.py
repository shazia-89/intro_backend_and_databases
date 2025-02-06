# hw_3/todos/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from .forms import TodoForm

def todos_list(request):
    todos = Todo.objects.all()  # Fetch all todos from the database
    return render(request, 'todos/todos_list.html', {'todos': todos})

# GET /todos/:id
def todo_detail(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        return JsonResponse({"todo": {
            "title": todo.title,
            "description": todo.description,
            "due_date": todo.due_date,
            "status": todo.status
        }})
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Todo not found"}, status=404)

# POST /todos/
@csrf_exempt  # Use CSRF exempt for simplicity
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Todo created successfully!"}, status=201)
        else:
            return JsonResponse({"error": "Invalid data"}, status=400)
    return JsonResponse({"error": "POST method required"}, status=405)

# DELETE /todos/:id/delete
def todo_delete(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('todos:todos_list')  # Redirect to the main page
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Todo not found"}, status=404)
