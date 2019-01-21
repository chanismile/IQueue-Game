from django import forms
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from trivia.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

def main_screen(request):
    return render(request, "trivia/main_screen.html")


def player_welcome(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.instance.save()
            return redirect(form.instance)
    else:
        form = PlayerForm()

    return render(request, "trivia/player_welcome.html", {
        'form': form,
    })


def player_answers(request):
    return render(request, "trivia/player_answers.html")
