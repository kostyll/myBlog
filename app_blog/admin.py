from django.contrib import admin
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse
from django.contrib.flatpages.models import FlatPage
 
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor.widgets import CKEditorWidget

from app_blog.models import blogPost, postComment


class blogPostForm(ModelForm):
    class Meta:
        model = blogPost
        fields = ('title','body','date')
        #widgets = {
        #           'body': TinyMCE(
        #                        attrs={'cols': 80, 'rows': 30},
        #                        #mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
        #                        )
        #           }
        widgets = { 'body': CKEditorWidget(attrs={'cols':50, 'rows':25})}
        
    fields = ('title','body',)
    readonly_fields = tuple()
    
class blogPostAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    form = blogPostForm

 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
 
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
 
 
# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(blogPost, blogPostAdmin)
admin.site.register(postComment)