from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/go-away/')
def index(request):
    tasks = Task.objects.all().order_by('-created' )
    form = TaskForm()
    detail_form = DetailTaskForm(initial={'category': ['15']})

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    
    if request.method == "POST":
        detail_form = DetailTaskForm(request.POST)
        if detail_form.is_valid:
            detail_form.save()
        return redirect('/')



    context = { 'tasks': tasks, 'form': form, 'detail_form':detail_form,}
    return render(request, 'list.html', context)

@login_required(login_url='/go-away/')
def detailTask(request):
    detail_form = DetailTaskForm(initial={'category': ['15']})
    if request.method == "POST":
        detail_form = DetailTaskForm(request.POST)
        if detail_form.is_valid:
            detail_form.save()
        return redirect('/')
    context = {'detail_form':detail_form,}
    return render(request, 'list.html', context)

@login_required(login_url='/go-away/')
def testView(request):
    tasks = Task.objects.all().order_by('complete')
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    # completed = request.POST.get('newsletter_topimage')

    
    
    print(Task.title)

    context = { 
        'tasks': tasks, 
        'form': form, 
        # 'extra_info_check': extra_info_check, 
    }
    return render(request, 'test.html', context)
@login_required(login_url='/go-away/')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update_task.html', context)

@login_required(login_url='/go-away/')
def taskDelete (rquest, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/')

@login_required(login_url='/go-away/')
def taskTicked (rquest, pk):
    item = Task.objects.get(id=pk)
    item.complete = True
    item.save()
    return redirect('/')

@login_required(login_url='/go-away/')
def taskUnticked (rquest, pk):
    item = Task.objects.get(id=pk)
    item.complete = False
    item.save()
    return redirect('/')

@login_required(login_url='/go-away/')
def searchView (request):
    query = request.GET.get('search')
    tasks = Task.objects.filter(title__icontains=query).order_by('title')

    if len(tasks) == 0:
        results = False
    else:
        results = True

    context = {'tasks': tasks, 'query': query, 'results': results,}
    return render(request, 'search.html', context)


def goawayView (request):

    return render(request, 'goaway.html')