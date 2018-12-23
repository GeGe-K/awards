from django.shortcuts import render, redirect
from .forms import UploadSiteForm, ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Review

# Create your views here.
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user = request.user).exists():
            Profile.objects.create(user = user)   
    projects = Project.objects.all()
    return render(request,"index.html",{"projects":projects})

def project(request, id):
    project = Project.objects.get(id = id)
    reviews = Review.objects.filter(project = project)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.save()
        return redirect('project')
    else:
        form = ReviewForm()
    return render(request, 'project.html', {'project': project, 'reviews': reviews, 'form': form})

@login_required(login_url='/accounts/login/')
def upload_site(request):
    if request.method == 'POST':
        form = UploadSiteForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
        return redirect('index')
    else:
        form = UploadSiteForm()

    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})

def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        projects = Project.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'projects': projects, 'message': message})
        
    return render(request, 'search.html')

@login_required(login_url='/accounts/login/')
def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
        return redirect('index')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})


