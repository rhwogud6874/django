from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')

    # print(title, content, due_date)

    # todo = Todo()
    # todo.title = title
    # todo.content = content
    # todo.due_date = due_date
    # todo.save()

    todo = Todo(title=title, content=content, due_date=due_date)
    todo.save()

    # return render(request, 'create.html')
    return redirect('/todos/')


def index(request):
    todos = Todo.objects.order_by('-due_date').all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    print(todo)
    return render(request, 'detail.html', context)


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todos/')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'edit.html', context)

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.title = request.GET.get('title')
    todo.content = request.GET.get('content')
    todo.due_date = request.GET.get('due-date')
    todo.save()
    return redirect(f'/todos/{todo_id}/')