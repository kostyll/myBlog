#coding: utf-8
from __future__ import unicode_literals
from app_blog.models import blogPost
from django.contrib.auth.forms import AuthenticationForm
from blog.settings import USER_REGISTRATION

def processor_login_form(request):
	if request.user.is_authenticated():
		print ('Authenticated')
		return {}
	else:
		if USER_REGISTRATION:
			print ('Not Authenticated')
			form = AuthenticationForm()
			return {'authForm':form,}
		else:
			return {}

def processor_user(request):
	return {'user':request.user,}

def processor_years(request):
	years = list(set([entry.date.year for entry in blogPost.objects.filter(active=True)]))
	return {'years':years,}