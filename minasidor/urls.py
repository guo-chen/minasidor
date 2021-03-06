from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from blog.views import HomeView, AboutView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minasidor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name="about"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^blog/', include('blog.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
