from django.contrib import admin
from modeltranslation.admin import TranslationAdmin 
from .models import Post


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'about', 'content', 'publish', 'source')
    list_display_links = ('title', )
