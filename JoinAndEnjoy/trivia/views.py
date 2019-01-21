from datetime import time

from django import forms
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from trivia.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

def main_screen(request):

    if request.method == "GET":
        request.session['answer'] = 1
    return render(request, "trivia/main_screen.html")

def main_screen_answers(request):
    return render(request,'trivia/main_screen_answers.html')


def player_welcome(request):
    if request.method == "POST":

        form = PlayerForm(request.POST)

        if form.is_valid():
            form.instance.save()
            return redirect(player_answers)
    else:
        form = PlayerForm()

    return render(request, "trivia/player_welcome.html", {
        'form': form,
    })

def player_answers(request):
    ans = ""
    if request.method == "POST":
        if request.session.has_key('answer'):
            ans = request.session['answer']
        if request.POST.get('choice') == ans:
            active = 'active_correct'
        else:
            active = 'active_incorrect'
        active_view = {
            'active': active
        }

    return render(request, "trivia/player_answers.html", active_view)


