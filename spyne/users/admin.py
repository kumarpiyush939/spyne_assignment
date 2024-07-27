from django.contrib import admin
from .models import SpyneUser as User

# Register your models here.
# admin.site.register(User)


@admin.register(User)
class ArticleAdmin(admin.ModelAdmin):
 list_display = ['name', 'mobile_no', 'email']
