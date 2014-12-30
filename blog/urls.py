from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogArchiveView.as_view(), name='blogs'),
    url(r'^details/(?P<article_id>\d+)', views.BlogDetailView.as_view(), name='blog_details'),
)
