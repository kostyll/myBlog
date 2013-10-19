# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admindocs    
#from django.contrib.admin.models import User
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.

class blogPost(models.Model):
    title = models.CharField(verbose_name=u"Заголовок", max_length=140)
    body = models.TextField(verbose_name=u"Текст посту")
    date = models.DateField(verbose_name=u"Дата")
    active = models.BooleanField(verbose_name=u"Відкритий", default=False)
    reviews = models.IntegerField(verbose_name=u'Кількість переглядів', default=0)

    def add_one_review(self):
    	self.reviews = self.reviews + 1
    	self.save()
    
    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
    	return self.title


class postComment(models.Model):
	author = models.ForeignKey(User, verbose_name=u"Автор")
	post = models.ForeignKey(blogPost,verbose_name=u"Пост")
	#comment = models.TextField(verbose_name=u"Коментарий")
	comment = RichTextField(verbose_name=u"Коментар")
	date = models.DateField(verbose_name=u"Дата")

	class Meta:
		pass

	def __unicode__(self):
		return self.comment[:20]

