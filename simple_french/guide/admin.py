from django.contrib import admin

from .models import Article, TableOfContentsNode

# Register your models here.
admin.site.register([Article, TableOfContentsNode])
