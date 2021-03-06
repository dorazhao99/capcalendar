from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from meals.models import *
from .forms import *
import datetime

# Handles 404 Requests
def handle404(request, exception):
    return redirect('page404')

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/meals/')
    else:
        return HttpResponse('<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p><a href="/accounts/login">Login</a></p>')
#------------------------------------------------------------------------------#
# STUDENT
#------------------------------------------------------------------------------#
# returns the meals for the current day
# @login_required
# @member_only
def current_day(request):
    day = datetime.datetime.today().weekday()
    if day == 5 or day == 6:
        day = 0
    lunch = Items.objects.filter(day_id=day, meal_id=0)
    if len(lunch) > 1:
        return HttpResponse('FIX')
    elif len(lunch) == 0:
        lunch = ''
    else:
        lunch = lunch[0].item.splitlines()
    dinner = Items.objects.filter(day_id=day, meal_id=1)
    if len(dinner) > 1:
        return HttpResponse('FIX')
    elif len(dinner) == 0:
        dinner = ''
    else:
        dinner = dinner[0].item.splitlines()
    template = loader.get_template('meals/menu.html')
    context = {
        'lunch_list': lunch,
        'dinner_list': dinner,
        'active': day,
    }
    return HttpResponse(template.render(context, request))

# returns for selected days of the week
# @login_required
# @member_only
def day_meal(request, day):
    lunch = Items.objects.filter(day_id=day, meal_id=0)
    if len(lunch) > 1:
        return HttpResponse('FIX')
    elif len(lunch) == 0:
        lunch = ''
    else:
        lunch = lunch[0].item.splitlines()
    dinner = Items.objects.filter(day_id=day, meal_id=1)
    if len(dinner) > 1:
        return HttpResponse('FIX')
    elif len(dinner) == 0:
        dinner = ''
    else:
        dinner = dinner[0].item.splitlines()
    template = loader.get_template('meals/menu.html')
    context = {
        'lunch_list': lunch,
        'dinner_list': dinner,
        'active': day,
    }
    return HttpResponse(template.render(context, request))
#------------------------------------------------------------------------------#
# ADMIN
#------------------------------------------------------------------------------#
# returns the meals for the current day
# @login_required
# @staff_only
def staff_current_day(request):
    day = datetime.datetime.today().weekday()
    if day == 5 or day == 6:
        day = 0
    lunch = Items.objects.filter(day_id=day, meal_id=0)
    if len(lunch) > 1:
        return HttpResponse('FIX')
    elif len(lunch) == 0:
        lunch = ''
    else:
        lunch = lunch[0].item.splitlines()
    dinner = Items.objects.filter(day_id=day, meal_id=1)
    if len(dinner) > 1:
        return HttpResponse('FIX')
    elif len(dinner) == 0:
        dinner = ''
    else:
        dinner = dinner[0].item.splitlines()
    template = loader.get_template('meals/staffmenu.html')
    context = {
        'lunch_list': lunch,
        'dinner_list': dinner,
        'active': day,
    }
    return HttpResponse(template.render(context, request))

# returns for selected days of the week
# @login_required
# @staff_only
def staff_meals(request, day):
    lunch = Items.objects.filter(day_id=day, meal_id=0)
    if len(lunch) > 1:
        return HttpResponse('FIX')
    elif len(lunch) == 0:
        lunch = ''
    else:
        lunch = lunch[0].item.splitlines()
    dinner = Items.objects.filter(day_id=day, meal_id=1)
    if len(dinner) > 1:
        return HttpResponse('FIX')
    elif len(dinner) == 0:
        dinner = ''
    else:
        dinner = dinner[0].item.splitlines()
    template = loader.get_template('meals/staffmenu.html')
    context = {
        'lunch_list': lunch,
        'dinner_list': dinner,
        'active': day,
    }
    return HttpResponse(template.render(context, request))

# @login_required
# @staff_only
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            day = form.cleaned_data['day_id']
            meal = form.cleaned_data['meal_id']
            object = Items.objects.filter(day_id=day, meal_id=meal)
            if len(object) <= 1:
                object.delete()
            item.save()
            return HttpResponseRedirect('/meals')
    else:
        form = ItemForm()

    return render(request, 'meals/add.html', {'form': form})

# @login_required
# @staff_only
def edit_item(request, day, meal):
    object = Items.objects.filter(day_id=day, meal_id=meal)
    instance = get_object_or_404(Items, id=object[0].id)
    form = ItemForm(request.POST or None, instance=instance)
    print(form)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        url = '/staff/meals/' + str(day)
        return HttpResponseRedirect(url)
    else:
        form = ItemForm(instance=instance)
    return render(request, 'meals/edit.html', {'form': form})
