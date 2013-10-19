from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from requestMeals.models import userDefaultMeals, userMeals

from blog.general_tools import today

@login_required
def viewRequestsMeals(request):
	group = request.user.groups.all()[0]
	print (group.name)
	users = group.user_set.all()
	meals = userMeals.objects.filter(date=today, user__in=users)
	print (meals.count())

	return render_to_response('requestsMeals.html',{'mealsList':meals},
        context_instance=RequestContext(request))
