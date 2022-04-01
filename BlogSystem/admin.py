from django.contrib import admin

from .models import User,Tag,Article

# Register your models here.
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article)