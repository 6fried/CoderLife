from django.shortcuts import render, get_list_or_404, get_object_or_404, render, redirect
from django.views import generic
from .models import Project
from taggit.models import Tag

def index(request, tag_slug=None):
    projects = Project.objects.all()
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        projects = get_list_or_404(Project, tags=tag)
    
    return render(request, 'showcase/index.html', {'project_list':projects, 'tag':tag})

class DetailView(generic.DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'showcase/project_detail.html'