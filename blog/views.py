from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import Article
from blog.models import Author
from blog.models import Category


# Create your views here.
def list_articles(request):
    articles = Article.objects.all().order_by('-publish_time')

    return render_to_response('blog/home.html', {'articles': articles}, context_instance=RequestContext(request))
