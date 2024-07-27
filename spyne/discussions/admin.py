from django.contrib import admin
from .models import Discussion

@admin.register(Discussion)
class ArticleAdmin(admin.ModelAdmin):
 list_display = ['text', 'image', 'hashtags', 'created_on', 'user']