from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Optional: Define a simple view to handle the root path
def home(request):
    return HttpResponse("<h1>Welcome to the Todo App</h1><p><a href='/todos/'>Go to Todos</a></p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),  # This is the route for the 'todos' app
    path('', home),  # This is the route for the root URL
]
