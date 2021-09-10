from django.shortcuts import render,redirect
from .models import Task,Comments
from .forms import TaskForm, CommentsForm
# Create your views here.
def index(request):
    tasklist = Task.objects.all()
    context = {'tasklist': tasklist}
    return render(request, 'taskapp/index.html', context)

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('taskapp:index')
        else:
            print('form is not valid',form)
    else:
        form = TaskForm(request.GET or None)
    return render(request, 'taskapp/create_task.html',{'form': form})

def editTask(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        datecreated = task.datecreated
        form.datecreated = datecreated
        print(form)
        if form.is_valid():
            task = form.save()
            return redirect('taskapp:index')
        else:
            print('form is not valid',form)
    else:
        form = TaskForm(instance = task)
    return render(request, 'taskapp/create_task.html',{'form': form})

def viewTask(request,pk):
    task = Task.objects.get(pk=pk)
    comments = Comments.objects.filter(task_id=pk)
    # print(comments)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save()
        else:
            print('form is not valid',form)
    else:
        form = CommentsForm(request.GET or None)
    return render(request, 'taskapp/view_task.html',{'task': task,'comments': comments,'form':form})