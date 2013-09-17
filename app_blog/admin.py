from django.contrib import admin
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse

from app_blog.models import blogPost, postComment


class blogPostForm(ModelForm):
    class Meta:
        model = blogPost
        fields = ('title','body','date')
        widgets = {
                   'body': TinyMCE(
                                attrs={'cols': 80, 'rows': 30},
                                #mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
                                )
                   }
        
    fields = ('title','body',)
    readonly_fields = tuple()
    
class blogPostAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    form = blogPostForm


admin.site.register(blogPost, blogPostAdmin)
admin.site.register(postComment)