from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'daily' # 'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
    priority = 0.9
    
    def items(self):

        return Post.objects.filter(status='published')
    def lastmod(self, obj):
        return obj.updated_at