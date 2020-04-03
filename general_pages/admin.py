# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
admin.site.register(TermsPolicy, SomeModelAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactUs._meta.fields]

    class Meta:
            model = ContactUs


admin.site.register(ContactUs, ContactUsAdmin)