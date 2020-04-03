# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
admin.site.register(BlogPost, BlogPostAdmin)


class BlogCategoryAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
admin.site.register(BlogCategory, BlogCategoryAdmin)
