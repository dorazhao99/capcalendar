from django import forms
from meals.models import *
from django.utils.translation import gettext_lazy as _

DAYS = [
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
]

MEALS = [
    (0,'Lunch'),
    (1, 'Dinner'),
]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('day_id', 'meal_id', 'item')
        labels = {
            'day_id': _('Day of the Week'),
            'meal_id':_('Meal'),
            'item':_('Items'),
        }
        DAY_CHOICES = (
            (0, 'Monday'),
            (1, 'Tuesday'),
            (2, 'Wednesday'),
            (3, 'Thursday'),
            (4, 'Friday'),
        )
        MEAL_CHOICES = (
            (0,'Lunch'),
            (1, 'Dinner'),
        )
        widgets = {
            'day_id': forms.Select(choices=DAY_CHOICES),
            'meal_id': forms.RadioSelect(choices=MEAL_CHOICES),
            'item': forms.Textarea(),
        }
