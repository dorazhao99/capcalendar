from django.contrib.auth.decorators import user_passes_test
from models import Members
from django.core.exceptions import ObjectDoesNotExist


# Decorator for views that checks that the user is a member not a bickeree
def member_only(function=None):
    actual_decorator = user_passes_test(
        is_member,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

# Decorator for views that checks that the user is a staff (special member :) )
def staff_only(function=None):
    actual_decorator = user_passes_test(
        is_staff,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def is_member(u):
    if u.is_staff or u.is_superuser:
        return True
    try:
        Members.objects.get(user=u)
    except ObjectDoesNotExist:
        return False
    return True

def is_staff(u):
    if u.is_staff or u.is_superuser:
        return True
    else:
        return False
