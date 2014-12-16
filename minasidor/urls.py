from django.conf.urls import patterns, include, url
from django.contrib import admin
# from ckeditor import urls

from blog import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minasidor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'blog.views.list_articles', name='list_articles'),
)
