from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
    '',
    url(r'^archives$', views.BlogArchives.as_view()),
    url(r'^details/(?P<article_id>\d+)', views.show_article_details, name='blog_details'),
)
