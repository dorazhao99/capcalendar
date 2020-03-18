from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from meals.models import *
import datetime
# # Handles 404 Requests
# def handle404(request, exception):
#     return redirect('page404')

def index(request):
    return HttpResponse("I fucked this up before")
#------------------------------------------------------------------------------#
# STUDENT
#------------------------------------------------------------------------------#
# returns the meals for the current day
def current_day(request):
    day = datetime.datetime.today().weekday()
    if day == 5 or day == 6:
        day = 0
    lunch = Items.objects.filter(day_id=day, meal_id=0)
    dinner = Items.objects.filter(day_id=day, meal_id=1)
    template = loader.get_template('meals/menu.html')
    context = {
        'lunch_list': lunch,
        'dinner_list': dinner,
    }
    return HttpResponse(template.render(context, request))

# returns for selected days of the week
def day_meal(request, day):
    lunch = Items.objects.filter(day_id=day, meal_id=0)
    dinner = Items.objects.filter(day_id=day, meal_id=1)
    template = loader.get_template('meals/menu.html')
    context = {
        'lunch_list': lunch,
        'dinner_list': dinner,
    }
    return HttpResponse(template.render(context, request))
#------------------------------------------------------------------------------#
# ADMIN
#------------------------------------------------------------------------------#
