#!/usr/bin/python
# -*- encoding: utf-8 -*-
 
from django.db.models import Field
from django.forms import Textarea
from blog.settings import MEDIA_URL
 
class WidgetWYSIWYG(Textarea):
    def __init__(self, *args, **kwargs):
        super(WidgetWYSIWYG, self).__init__(attrs={'class': 'wysiwygEditor vLargeTextField'}, *args, **kwargs)
    class Media:
        js = (
            MEDIA_URL+'tiny_mce/tiny_mce.js',
            MEDIA_URL+'filebrowser/js/TinyMCEAdmin.js',
            )
 
class WYSIWYGField(Field):
    def get_internal_type(self):
        return "TextField"
 
    def formfield(self, **kwargs):
        defaults = {'widget': WidgetWYSIWYG}
        defaults.update(kwargs)
        return super(WYSIWYGField, self).formfield(**defaults)