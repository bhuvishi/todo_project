from django.shortcuts import render, redirect
from .forms import SingleTODOForm

from .models import SingleTODO

def home_page(request):
    context = {'todos': SingleTODO.objects.all()}
    return render(request, 'todo/home.html', context)

def about_page(request):
    return render(request, 'todo/about.html')

def add_todo(request):
    if request.method == 'POST':
        form = SingleTODOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
    else:
        form = SingleTODOForm()
    return render(request, 'todo/add-todo.html', {'form': form})

def update_todo(request, todo_id):
    todo_object = SingleTODO.objects.get(id=todo_id)
    todo_object.complete = not todo_object.complete
    todo_object.save()
    return redirect('todo-home')

def delete_todo(request, todo_id):
    SingleTODO.objects.filter(id=todo_id).delete()
    return redirect('todo-home')