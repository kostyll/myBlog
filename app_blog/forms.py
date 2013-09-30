from django import forms
from django.forms import fields
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from app_blog import widgets

from crispy_forms.helper import FormHelper

class commentPost(forms.Form):
	comment = forms.fields.CharField(label=u"",widget=CKEditorWidget(attrs={'cols':50, 'rows':25}))
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		super(commentPost,self).__init__(*args,**kwargs)


	

