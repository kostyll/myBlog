#coding: utf-8
from __future__ import unicode_literals
from app_blog.models import blogPost
from django.contrib.auth.forms import AuthenticationForm

def processor_login_form(request):
	years = list(set([entry.date.year for entry in blogPost.objects.all()]))
	form = AuthenticationForm()
	return {'years':years, 'user':request.user,'authForm':form}
