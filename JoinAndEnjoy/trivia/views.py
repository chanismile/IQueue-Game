import datetime
from datetime import time
from django.utils import timezone

from django import forms
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect

from trivia.models import Player, Question, CurrentQuestion

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

def main_screen(request, first_time =False, second_time=False):
    # if first_time:
    #     if datetime.datetime.now() <= CurrentQuestion.objects.get(q=1).answering_end:
    #         if second_time:
    #             if datetime.datetime.now() <= CurrentQuestion.objects.get(q=1).answering_end:
    #                 return redirect("main_screen", False, False)
    #             else:
    #                 return redirect("main_screen", True, True)
    #         else:
    #             render(request, "trivia/main_screen_answers.html")
    #             now = datetime.datetime.now().strftime('%H:%M:%S')
    #             CurrentQuestion.objects.filter(q=1).update(display_end=now + 5)
    #             return redirect("main_screen", first_time, True)
    #
    # else:
    #     o = Question.objects.get(pk=1)
    #     now = datetime.datetime.now().strftime('%H:%M:%S')
    #     c = CurrentQuestion.objects.filter(q=1).update(question=o,answering_end=now+5)
    #     first_time = True

    render(request, "trivia/main_screen.html")
    return redirect("main_screen", first_time, second_time)


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
    end_time = CurrentQuestion.objects.first().answering_end
    if timezone.now() > end_time:
        active = ''#
        if request.method == "POST":
            print(f"date: $$$$$$$$$$$$$$$$$$$")
            request.session['player_choice'] = request.POST.get('choice')
            # return redirect("player_choices")
        elif request.POST.get('choice'):
            active = 'active_wait'

        # else:
        #     return redirect("player_choices")

        # render(request, "trivia/player_choices", active_view)
        # return redirect("player_choices")
    # else:
    #     cq = CurrentQuestion.objects.get(q=1)
    #     # q = Question.objects.get(id=cq.question)
    #     correct_answer = cq.question.correct_choice
    #
    #     if request.POST.get('choice') == correct_answer:
    #         active = 'active_correct'
    #     else:
    #         active = 'active_incorrect'
    #     active_view = {
    #         'active': active
    #     }
    return render(request, "trivia/player_choices.html")

    # return render(request, "trivia/player_choices.html", active_view)


