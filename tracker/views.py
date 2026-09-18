from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import JobApplication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import JobApplicationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('application_list')
        else:
            messages.error(request, 'Registration failed. Please check the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'tracker/list.html', {'applications': applications})


@login_required
def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/add.html', {'form': form})