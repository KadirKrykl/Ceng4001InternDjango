from django.shortcuts import render,HttpResponse, get_object_or_404

from .models import ResearchGroups, News, UserProfile, Research, Resource, Publication, Project
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.

def index(requests):
    return render(requests,'index.html')

#---------------------------------
#+++++++++++++++NEWS++++++++++++++
#---------------------------------

def news_list(requests):
    news_list = News.objects.filter(draft=False)
    rsg_list = ResearchGroups.objects.all()
    return render(requests,'news/list.html',context={'posts':news_list,'groups':rsg_list})

def news_list_filter_group(requests,slug):
    group = get_object_or_404(ResearchGroups,slug=slug)
    news_list = News.objects.filter(researchGroup=group,draft=False)
    rsg_list = ResearchGroups.objects.all()
    return render(requests,'news/list.html',context={'posts':news_list,'groups':rsg_list})

def news_details(requests,slug):
    news = get_object_or_404(News,slug=slug)
    return render(requests,'news/detail.html',context={'post':news})


#---------------------------------
#++++++++++USER_PROFILES++++++++++
#---------------------------------

def profiles_list(requests):
    profiles = UserProfile.objects.filter()
    titles = Group.objects.all()
    return render(requests,'people/list.html',context={'posts':profiles,'titles':titles})

def profiles_details(requests,slug):
    people = get_object_or_404(UserProfile,slug=slug)
    return render(requests,'people/detail.html',context={'post':people})

#---------------------------------
#+++++++++++++PROJECT+++++++++++++
#---------------------------------

def project_list(requests):
    project_list = Project.objects.filter(draft=False)
    rsg_list = ResearchGroups.objects.all()
    return render(requests,'project/list.html',context={'posts':project_list,'groups':rsg_list})

def project_list_filter_group(requests,slug):
    group = get_object_or_404(ResearchGroups,slug=slug)
    project_list = Project.objects.filter(researchGroup=group,draft=False)
    rsg_list = ResearchGroups.objects.all()
    return render(requests,'project/list.html',context={'posts':project_list,'groups':rsg_list})

def project_details(requests,slug):
    project = get_object_or_404(Project,slug=slug)
    return render(requests,'project/detail.html',context={'post':project})


#---------------------------------
#+++++++++++++RESEARCH++++++++++++
#---------------------------------

def research_list(requests):
    research_list = Research.objects.filter(draft=False)
    rsg_list = ResearchGroups.objects.all()
    return render(requests,'research/list.html',context={'posts':research_list,'groups':rsg_list})

def research_list_filter_group(requests,slug):
    group = get_object_or_404(ResearchGroups,slug=slug)
    research_list = Research.objects.filter(researchGroup=group,draft=False)
    rsg_list = ResearchGroups.objects.all()
    return render(requests,'research/list.html',context={'posts':research_list,'groups':rsg_list})

def research_details(requests,slug):
    research = get_object_or_404(Research,slug=slug)
    return render(requests,'research/detail.html',context={'post':research})

#---------------------------------
#++++++++++PUBLICATION++++++++++++
#---------------------------------

def publication_list(requests):
    research_list = Publication.objects.all()
    years = [item.year for item in research_list]
    years = list(set(years))
    years.reverse()
    return render(requests,'publication/list.html',context={'posts':research_list,'years':years})
    
#---------------------------------
#++++++++++++RESOURCE+++++++++++++
#---------------------------------

def resource_list(requests):
    resource_list = Resource.objects.all()
    return render(requests,'resource/list.html',context={'posts':resource_list})