# -*- coding: utf-8 -*-
# Create your views here.

from __future__ import unicode_literals

from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from app_blog.models import blogPost, postComment
from app_blog.forms import commentPost
from django.template.defaulttags import autoescape
from django.shortcuts import render, render_to_response

from django import template

register = template.Library()

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login

from django.contrib.auth import login as auth_login, authenticate
from django.template import RequestContext

from blog.general_tools import today


def prepareContext(context_instance = None, context_variable = None):
    if context_variable is None:
        return context_instance
    if context_instance is None:
        context_instance = dict(**context_variable)
    else:
        context_instance.update(**context_variable)
    return context_instance

def prepareTitle(context_instance, title):
    return prepareContext(context_instance=context_instance, context_variable = {'title':title,})

def viewYearPosts(request, year = today.year):
    posts = blogPost.objects.filter(date__year = year, active=True)
    pageTemplate = loader.get_template("index.html")
    pageContext = {'posts':posts, }
    pageContext = prepareTitle(pageContext, 'Останні пости')
    return render_to_response("index.html",pageContext,
        context_instance=RequestContext(request))

def viewPost(request, post=0):
    content = blogPost.objects.get(id=post)
    content.add_one_review()
    comments = postComment.objects.filter(post=content)
    pageTemplate = loader.get_template("viewPost.html")
    pageContext = {'post': content, 'comments':comments, }
    pageContext = prepareTitle(pageContext, content.title)
    return render_to_response("viewPost.html", pageContext,
        context_instance=RequestContext(request))

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
        pageContext = {'form':form, 'redirect':post, }
        pageContext = prepareTitle(pageContext, 'Відправити коментар')
    return render(request,"putComment.html", pageContext)

def viewLogout(request):
    logout(request,next_page='/')
    return HttpResponseRedirect('/')

def viewLogin(request):
    username = password = ''
    if request.POST :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect('/')
        else:
            form = AuthenticationForm(request)
            pageContext = {
                 'form': form,
                redirect_field_name: redirect_to,
                'site': current_site,
                'site_name': current_site.name,
            }
            pageContext = prepareTitle(pageContext, 'Увійти')
            return TemplateResponse(request, "login.html", RequestContext(pageContext),)
    else:
        #!!!!!!!!!!!!!!!!!!!
        return HttpResponseRedirect('/')
        #!!!!!!!!!!!!!!!!!!!

def registerAgree(request):
    pass