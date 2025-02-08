from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

# List all Todos (GET todos/)
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# View a single Todo (GET todos/:id)
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# Add a new Todo (POST todos/)
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/add_todo.html', {'form': form})

# Delete a Todo (DELETE todos/:id/delete)
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
