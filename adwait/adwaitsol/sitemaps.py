from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from adwaitsol.models import AdwaitappBlogs

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['', 'about', 'contact']
    
    def location(self, item):
        return reverse(item)
    
class PostViewSitemap(Sitemap):
    def items(self):
        return AdwaitappBlogs.objects.order_by('-creation_date')