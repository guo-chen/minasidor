from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
# Generic class-based views
from django.views.generic.base import TemplateView

# Django's paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Article
from blog.models import Author
from blog.models import Category


# Create your views here.
def list_articles(request):
    articles = Article.objects.all().order_by('-publish_time')

    return render_to_response('blog/home.html', {'articles': articles}, context_instance=RequestContext(request))


def show_article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    return render_to_response('blog/details.html', {'article': article}, context_instance=RequestContext(request))


def home_list_blogs(request):
    article_list = Article.objects.all().order_by('-publish_time')
    paginator = Paginator(article_list, 5)  # Show 5 blogs in a page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render_to_response('blog/home.html', {'articles': articles}, context_instance=RequestContext(request))


class BlogArchives(TemplateView):
    template_name = "blog/blog_archives.html"
    model = Article

    def get_context_data(self, **kwargs):
        archives = {}
        context = super(BlogArchives, self).get_context_data(**kwargs)
        years = Article.objects.all().datetimes('publish_time', 'year')[::-1]
        for date_year in years:
            months = Article.objects.all().filter(publish_time__year=date_year.year).datetimes('publish_time', 'month')
            archives[date_year] = months
        context['archives'] = sorted(archives.items(), reverse=True)
        return context


class HomeView(TemplateView):
    template_name = "blog/home.html"

    # Add the context for 'archives'
    def get_context_data(self, **kwargs):
        archives = {}
        context = super(TemplateView, self).get_context_data(**kwargs)
        years = Article.objects.all().datetimes('publish_time', 'year')[::-1]
        for date_year in years:
            months = Article.objects.all().filter(publish_time__year=date_year.year).datetimes('publish_time', 'month')
            archives[date_year] = months
        context['archives'] = sorted(archives.items(), reverse=True)
        return context

    def get(self, request):
        article_list = Article.objects.all().order_by('-publish_time')
        paginator = Paginator(article_list, 5)  # Show 5 blogs in a page
        page = request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context = self.get_context_data()
        context['articles'] = articles

        return render_to_response(self.template_name, context, context_instance=RequestContext(request))
    