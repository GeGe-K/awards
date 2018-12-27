from django.shortcuts import render, redirect
from .forms import UploadSiteForm, ReviewForm, UpdateProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Review
from django.urls import reverse
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user = request.user).exists():
            Profile.objects.create(user = user)   
    projects = Project.objects.order_by('-pub_date')
    return render(request,"index.html",{"projects":projects})

def project(request, id):
    project = Project.objects.get(id = id)
    reviews = Review.objects.filter(project = project)
    design = Review.objects.all().aggregate(Avg('design'))['design__avg']
    usability = Review.objects.all().aggregate(Avg('usability'))['usability__avg']
    content = Review.objects.all().aggregate(Avg('content'))['content__avg']
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.user = user
            review.save()
        return redirect(reverse('project'))
    else:
        form = ReviewForm()
    return render(request, 'project.html', {'project': project, 'reviews': reviews, 'form': form, 'design': design, 'usability': usability, 'content': content})

def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        projects = Project.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'projects': projects, 'message': message})
        
    return render(request, 'search.html')

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

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

def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})

@login_required(login_url = '/accounts/login/')
def update_profile(request, id):
    if request.method == 'POST':
        profile = Profile.objects.get(id = id)
        form = UpdateProfile(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateProfile()

    return render(request, 'update_profile.html', {'form': form})


