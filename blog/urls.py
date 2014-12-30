from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogsView.as_view(), name='blogs'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.BlogArchiveView.as_view(), name='blog_archive'),
    url(r'^details/(?P<article_id>\d+)$', views.BlogDetailView.as_view(), name='blog_details'),
)
