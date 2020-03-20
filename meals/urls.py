from django.urls import path

from . import views

urlpatterns = [
    path('', views.current_day, name='today'),
    path('<int:day>/', views.day_meal, name='day_meals'),
]
