from functools import total_ordering
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect 

from .models import Task
from .forms import *

# Create your views here.





def index(request):
    #return HttpResponse('Testing Passed') 

    if 'search' in request.GET:
        search=request.GET['search']
        tasks=Task.objects.filter(title__icontains=search)
    else:
        tasks=Task.objects.all()



    # tasks=Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = Task.objects.filter(complete=True) 
    total_completed_tasks = completed_tasks.count() 
    total_uncompleted_tasks = total_tasks - total_completed_tasks   
    form=TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={
        'tasks' :tasks, 
        'form' :form,
        'total_tasks' :total_tasks,
        'completed_tasks' :completed_tasks,
        'total_completed_tasks' :total_completed_tasks,
        'total_uncompleted_tasks' :total_uncompleted_tasks,

    
    }    
    return render(request, 'tasks/listt.html', context) 

#update 

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'form':form}
    return render(request, 'tasks/task_update.html', context)


#delete

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request, 'tasks/delete.html', context)


    




        
    #.also update your urls
    #kuno ukutsvagei
  
