# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from app_blog.models import blogPost, postComment
from app_blog.forms import commentPost
from django.template.defaulttags import autoescape
from django.shortcuts import render, render_to_response
from datetime import date 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login

from django.contrib.auth import login as auth_login
from django.template import RequestContext

today = date.today()

def prepareContext(request, context=None):
	years = list(set([entry.date.year for entry in blogPost.objects.all()]))
	form = AuthenticationForm()
	context.update(years=years, user=request.user, authForm=form)
	return context

def viewYearPosts(request, year = today.year):
	posts = blogPost.objects.filter(date__year = year)
	pageTemplate = loader.get_template("index.html")
	pageContext = prepareContext(request,{'posts':posts, })
	return render_to_response("index.html",pageContext,
		context_instance=RequestContext(request))
	#return HttpResponse(pageTemplate.render(pageContext)) 	

def viewPost(request, post=0):
	content = blogPost.objects.get(id=post)
	comments = postComment.objects.filter(post=content)
	pageTemplate = loader.get_template("viewPost.html")
	pageContext = Context(prepareContext(request,{'post': content, 'comments':comments }),autoescape=False)
	return HttpResponse(pageTemplate.render(pageContext))

@login_required
def putComment(request,post=0):
	if request.method == "POST":
		form = commentPost(request.POST)
		if form.is_valid():
			comment = postComment(
				author=request.user, 
				post=blogPost.objects.get(id=post), 
				comment=request.POST['comment'], 
				date=today
				)
			comment.save()
			return HttpResponseRedirect('/post/'+str(post)+'/')
	else:
		form = commentPost()
	return render(request,"putComment.html",prepareContext(request,{
		'form':form, 'redirect':post,
		}))

def viewLogout(request):
	logout(request,next_page='/')
	return HttpResponseRedirect('/')

def viewLogin(request):
	username = password = ''
	if request.POST :
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			auth_login(request,form.get_user())
			return HttpResponseRedirect('/')
		else:
			form = AuthenticationForm(request)
			context = {
		        'form': form,
		        redirect_field_name: redirect_to,
		        'site': current_site,
		        'site_name': current_site.name,
		    }
			return TemplateResponse(request, "login.html", RequestContext(context),
		                           )

def registerAgree(request):
	pass