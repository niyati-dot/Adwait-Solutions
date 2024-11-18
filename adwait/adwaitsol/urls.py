from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, PostViewSitemap

sitemaps = {'static': StaticViewSitemap, 'posts': PostViewSitemap}

urlpatterns = [
  path("robots.txt", TemplateView.as_view(template_name="adwaitsol/robots.txt", content_type="text/plain")),
  path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
  path('', views.home, name=""),
  path('contact', views.contact, name="contact"),
  path('about', views.about, name="about"),
  path('services', views.services, name="services"),
  path('service/<str:item_name>',views.render_items, name='service'),
  path('sub-service/<str:item_name>',views.render_submenu, name='sub-service'),
  path('blog/<str:item_name>',views.render_blogs, name='blog'),
  path('blogs', views.blogs, name="blogs"),
  path('portfolio', views.portfolio, name="portfolio"),
  path('subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
  path('inquiry/', views.inquiry, name='inquiry'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)