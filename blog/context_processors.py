#coding: utf-8
from __future__ import unicode_literals
from app_blog.models import blogPost
from django.contrib.auth.forms import AuthenticationForm

def processor_login_form(request):
	if request.user.is_authenticated:
		return {}
	else:
		form = AuthenticationForm()
		return {'authForm':form,}

def processor_user(request):
	return {'user':request.user,}

def processor_years(request):
	years = list(set([entry.date.year for entry in blogPost.objects.all()]))
	return {'years':years,}
