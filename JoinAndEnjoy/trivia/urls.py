from django.urls import path

from . import views

urlpatterns = [
    path('main', views.main_screen, name='main_screen'),
    path('main_screen_answers', views.main_screen_answers, name='main_screen_answers'),
    path('player_welcome', views.player_welcome, name='player_welcome'),
    path('player_choices', views.player_choices, name='player_choices'),
]