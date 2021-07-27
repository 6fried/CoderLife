from django.db import models
from taggit.managers import TaggableManager

class Project(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return f"/showcases/{self.slug}"

    def __str__(self):
        return self.name
