# -*- coding: utf-8 -*-
# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from app_blog.models import blogPost, postComment
from app_blog.forms import commentPost
from django.template.defaulttags import autoescape
from django.shortcuts import render
from datetime import date 

today = date.today()

def prepareContext(context=None):
	years = list(set([entry.date.year for entry in blogPost.objects.all()]))
	context.update(years=years)
	return context

def viewYearPosts(request, year = today.year):
	posts = blogPost.objects.filter(date__year = year)
	pageTemplate = loader.get_template("index.html")
	pageContext = Context(prepareContext({'posts':posts, }),autoescape=False)
	return HttpResponse(pageTemplate.render(pageContext)) 	

def viewPost(request, post=0):
	content = blogPost.objects.get(id=post)
	comments = postComment.objects.filter(post=content)
	pageTemplate = loader.get_template("viewPost.html")
	pageContext = Context(prepareContext({'post': content, 'comments':comments }),autoescape=False)
	return HttpResponse(pageTemplate.render(pageContext))

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
	return render(request,"putComment.html",prepareContext({
		'form':form, 'redirect':post,
		}))
