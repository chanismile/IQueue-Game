from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_screen, name='main_screen'),
    path('player_welcome', views.player_welcome, name='player_welcome'),
    path('player_answers', views.player_answers, name='player_answers'),
]