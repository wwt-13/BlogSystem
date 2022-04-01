from django.contrib import admin

from .models import Article, Tag, User

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article)