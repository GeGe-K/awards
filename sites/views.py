from django.shortcuts import render, redirect
from .forms import UploadSiteForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Project

# Create your views here.
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user = request.user).exists():
            Profile.objects.create(user = user)   
    projects = Project.objects.all()
    return render(request,"index.html",{"projects":projects})

@login_required(login_url='/accounts/login/')
def upload_site(request):
    if request.method == 'POST':
        form = UploadSiteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['sitename'])
    else:
        form = UploadSiteForm()

    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})


