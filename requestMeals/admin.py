from django.contrib import admin

from requestMeals import models

admin.site.register(models.userMeals)
admin.site.register(models.userDefaultMeals)