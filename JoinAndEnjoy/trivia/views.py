import datetime
from datetime import time

from django.http import HttpResponse
from django.utils import timezone
import pytz

from django import forms
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect

from trivia.models import Player, Question, CurrentQuestion, helper

import random

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


def main_screen(request):

    items = Question.objects.all()
    random_question = random.choice(items)
    CurrentQuestion.objects.filter(q=1).update(question=random_question)

    return render(request, "trivia/main_screen.html", {'question': random_question})


def main_screen_answers(request):
    question = CurrentQuestion.objects.first().question
    return render(request, 'trivia/main_screen_answers.html', {'question': question})


def player_welcome(request):

    if request.method == "POST":
        p = Player(name=request.POST['player_name'])
        request.session['player_id'] = p.id
        p.save()
        return redirect('player_choices')

    return render(request, "trivia/player_welcome.html")

    # TOCHECK - Chani
    # if request.method == "POST":
    #
    #     form = PlayerForm(request.POST)
    #
    #     if form.is_valid():
    #         form.instance.save()
    #         return redirect(player_answers)
    # else:
    #     form = PlayerForm()
    #
    # return render(request, "trivia/player_welcome.html", {
    #     'form': form,
    # })


def player_choices(request):
    question = CurrentQuestion.objects.first().question
    correct_choice = Question.objects.get(id=question.id).correct_choice
    return render(request, "trivia/player_choices.html", {'correct_choice': correct_choice, })




