from django.shortcuts import render
from todo.models import TodoList

# Create your views here.
def todos(request):
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/todos.html',
  		{
			'todolist': todolist,
		}
	)

def index(request):
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/index.html',
		{
			'todolist': todolist,
		}
	)
