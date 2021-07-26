from django.shortcuts import render
from django.db.models import Q
from blog.models import Post
from showcase.models import Project

def index(request):
    query = request.GET.get("q")
    if query:
        results=[Post.objects.filter(Q(title__icontains=query) | Q(tags__name__icontains=query), status='published').distinct(), Project.objects.filter(Q(name__icontains=query) | Q(tags__name__icontains=query)).distinct()]

        return render(request, 'search/index.html', {'results':results,})
    
    return render(request, 'index.html')