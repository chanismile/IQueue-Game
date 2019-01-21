from datetime import time

from django import forms
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from trivia.models import Player, Question, CurrentQuestion

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


def main_screen(request, first_time):
    # if (first_time):
    #     continue
    # else:
    #     o = Questions.objects.get(pk=1)
    #     c = CurrentQuestion()
    # if request.method == "GET":
    #     request.session['answer'] = 1
    return render(request, "trivia/main_screen.html")

def main_screen_answers(request):
    return render(request,'trivia/main_screen_answers.html')



def player_welcome(request):
    if request.method == "POST":
        p = Player.objects.create(name=request.POST['name'])
        request.session['player_id'] = p.id
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

    # if time isn't over
    if True:
        active = ''#
        if request.method == "POST":
            request.session['player_choice'] = request.POST.get('choice')
            # return redirect("player_choices")
        elif request.POST.get('choice'):
            active = 'active_wait'

        # else:
        #     return redirect("player_choices")

        # render(request, "trivia/player_choices", active_view)
        return redirect("player_choices")
    else:
        cq = CurrentQuestion.objects.get(pk=1)
        q = Question.objects.get(pk=cq.question)
        correct_answer = q.correct_choice

        if request.POST.get('choice') == correct_answer:
            active = 'active_correct'
        else:
            active = 'active_incorrect'
        active_view = {
            'active': active
        }
        return render(request, "trivia/player_choices.html", active_view)

    # return render(request, "trivia/player_choices.html", active_view)

