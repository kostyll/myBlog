#-*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User

class userDefaultMeals(models.Model):
	user = models.ForeignKey(User, verbose_name='Користувач')
	breakfast = models.BooleanField(default=True, verbose_name='Сніданок')
	supper = models.BooleanField(default=True, verbose_name='Вечеря')


#class userMeals(userDefaultMeals):
#	def __init__(self,*args, **kwargs):
#		super(userMeals,self).__init__(self,*args,**kwargs)
#
#	date = models.DateField(verbose_name='Дата')

class userMeals(models.Model):
	user = models.ForeignKey(User, verbose_name='Користувач')
	breakfast = models.BooleanField(default=True, verbose_name='Сніданок')
	supper = models.BooleanField(default=True, verbose_name='Вечеря')

	date = models.DateField(verbose_name='Дата')
