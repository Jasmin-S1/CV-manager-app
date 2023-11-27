from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm, JobSearchForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm   # ovo je built-in forma za kreiranje usera
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('all_jobs')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + user)
                return redirect('user_login')
            
        context = {'form': form}
        return render(request, 'jobs/register.html', context)



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('all_jobs')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
                
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('all_jobs')
            
            else:
                messages.info(request,'Username or Password is incorrect')
            
        context = {}
        return render(request, 'jobs/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('user_login')



@login_required(login_url='user_login')
def showJobs(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/index.html', {
        'jobs': jobs
    })



@login_required
def deleteJob(request, pk):
    if request.method == "POST":
        job = Job.objects.get(id=pk)
        job.delete()
        return redirect(request.GET.get('next', 'jobs:index'))
    return render(request, 'jobs/delete_job', {'job': job})



@login_required
def addJob(request):
    if request.method == 'POST':
        form  = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('all_jobs')
    else:
        form = JobForm()
    
    return render(request, 'index.html', {'form': form})



@login_required   
def searchJob(request):
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            jobTitle = form.cleaned_data['jobTitle']
            jobs = Job.objects.filter(jobTitle__icontains=jobTitle)
            return render(request, 'jobs/index.html', {'jobs': jobs, 'form': form})
    else:
        form = JobSearchForm()
        jobs = Job.objects.all()
        return render(request, 'jobs/index.html', {'jobs': jobs, 'form': form})
    


@require_POST
def toggleFeedback(request, job_id):
    job = Job.objects.get(id=job_id)
    job.feedback = not job.feedback
    job.save()
    return redirect('all_jobs')
