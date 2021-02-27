
from django.contrib import admin
from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, StaticViewSitemap

from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'posts': PostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
