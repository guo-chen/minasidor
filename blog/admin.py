from django.contrib import admin
from blog.models import Author, Article, Category, Tag


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    search_fields = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'subtitle',
                    'author',
                    'category',
                    'publish_time',
                    'update_time',
                    )
    list_filter = ('publish_time', )
    ordering = ('-publish_time', )
    filter_horizontal = ('tags', )
    # date_hierarchy = 'publish_time'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Tag)
