from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=50, blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    content = RichTextField(config_name="customized")
    number_of_clicks = models.IntegerField(u'Clicks', default=0)

    def incr_clicks(self):
        self.number_of_clicks += 1
        self.save()
