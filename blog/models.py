from django.db import models
from django.db.models.expressions import OrderBy
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class Post(models.Model):
    STATUT_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='pub_date')
    author = models.CharField(max_length=80)
    # description = models.TextField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    content = RichTextUploadingField(null=True)
    post_img = models.ImageField(upload_to='media', null=True)
    
    tags = TaggableManager()
    
    pub_date = models.DateTimeField('published date', default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10, choices=STATUT_CHOICES, default='draft')
    
    class Meta:
        ordering = ('-pub_date',)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_comments(self):
        return Comment.objects.filter(post=self).filter(active=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering=('created', )
    
    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)