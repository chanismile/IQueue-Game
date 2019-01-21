from django.urls import path

from . import views

urlpatterns = [
    path('main_screen', views.main_screen, name='main_screen'),
    path('player_welcome', views.player_welcome, name='player_welcome'),
    path('player_choices', views.player_choices, name='player_choices'),
]