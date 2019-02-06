from django.contrib import admin
from .models import Article

# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','tag','author','status','created')
    search_fields = ('title','body')
    ordering = ('title','-created',)
    list_filter = ('status','created','author')