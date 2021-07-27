from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Count


def index(request, tag_slug=None):
    posts = Post.objects.filter(status='published')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = get_list_or_404(Post, status='published', tags=tag)
    
    return render(request, 'blog/index.html', {'post_list':posts, 'tag':tag})

def post_detail(request, post_name):
    post = get_object_or_404(Post, slug=post_name, status='published')
    
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm()    
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url()+'#'+ str(new_comment.id))

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids, status='published').exclude(slug=post.slug)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-pub_date')[:6]

    return render(request, 'blog/post_detail.html', {'post':post, 'comments': comments, 'comment_form':comment_form, 'similar_posts':similar_posts})

def reply_page(request, slug, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            post_url = request.POST.get('post_url')

            post=get_object_or_404(Post, slug=slug)
            parent = get_object_or_404(Comment, id=comment_id)

            reply = form.save(commit=False)

            reply.post = post
            reply.parent = parent
            reply.save()
            
            return redirect(post_url + '#' + str(reply.id))

    return redirect(request.POST.get('post_url'))
