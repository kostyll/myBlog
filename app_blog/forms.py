from django import forms
from django.forms import fields
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from app_blog import widgets

class commentPost(forms.Form):
	comment = forms.CharField(widget=CKEditorWidget(attrs={'cols':50, 'rows':25}))
	pass

