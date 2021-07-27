from django.shortcuts import render, get_list_or_404, get_object_or_404, render, redirect
from django.views import generic
from .models import Showcase
from django.db.models import Q, Count
from taggit.models import Tag

def index(request, tag_slug=None):
    projects = Showcase.objects.all()
    
    query = request.GET.get("q")
    if query:
        projects=Showcase.objects.filter(Q(name__icontains=query) | Q(tags__name__icontains=query)).distinct()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        projects = get_list_or_404(Showcase, tags=tag)
    
    return render(request, 'showcase/index.html', {'project_list':projects, 'tag':tag})



class DetailView(generic.DetailView):
    model = Showcase
    context_object_name = 'project'
    template_name = 'showcase/project_detail.html'