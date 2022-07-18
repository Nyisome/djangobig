from functools import total_ordering
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required 



from .models import Task
from .forms import *
from .forms import CreateUserForm

# Create your views here.




#register

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account for'+ user ,'has been created')

                return redirect('login')
        
        context = {'form':form}
        return render(request, 'tasks/register.html',context)

#login 

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:

        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.info(request, 'Username or Password is incorrect')
                
        context = {}
        return render(request, 'tasks/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


#homepage
@login_required(login_url='login')
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


    




        
    #also update your urls
    #kuno ukutsvagei
  