import datetime
from datetime import time
from django.utils import timezone
import pytz

from django import forms
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect

from trivia.models import Player, Question, CurrentQuestion, helper


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


def main_screen(request):
    h = helper.objects.first()
    if h.first_time:
        print("ggggggggggg\n")
        utc = pytz.UTC
        answering_end = CurrentQuestion.objects.get(q=1).answering_end.replace(tzinfo=utc)
        now = datetime.datetime.now().replace(tzinfo=utc)
        if now > answering_end:
            if h.second_time:
                utc = pytz.UTC
                display_end = CurrentQuestion.objects.get(q=1).display_end.replace(tzinfo=utc)
                now2 = datetime.datetime.now().replace(tzinfo=utc)
                if now2 > display_end:
                    helper.objects.filter(i=1).update(first_time=0,second_time=0)
                    print("wowowowowo\n")
                    return redirect("main_screen")
                else:
                    helper.objects.filter(i=1).update(first_time=1,second_time=1)
                    print(f"bigbig {now} vs {display_end}\n")
                    # render(request, "trivia/main_screen_answers.html")
                    return redirect("main_screen")
            else:
                render(request, "trivia/main_screen_answers.html")
                now = datetime.datetime.now()
                total = now + datetime.timedelta(0,1)
                CurrentQuestion.objects.filter(q=1).update(display_end=total.replace(tzinfo=timezone.utc).astimezone(tz=None))
                print("display_end\n")

                helper.objects.filter(i=1).update(second_time=1)
                return redirect("main_screen")

    else:
        print("wewewewewewewewe\n")
        o = Question.objects.get(pk=1)
        # now = datetime.datetime.now()
        now = timezone.now()
        total = now + datetime.timedelta(0, 1)
        CurrentQuestion.objects.filter(q=1).update(question=o,answering_end=total.replace(tzinfo=timezone.utc).astimezone(tz=None))
        helper.objects.filter(i=1).update(first_time=1)
        print("upupup\n")
        # help = helper.objects.get(pk=1)
        # help.first_time = 1
        # help.save()
    render(request, "trivia/main_screen.html")

    return redirect("main_screen")



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
            request.session['player_choice'] = request.POST.get('choice')
            # return redirect("player_choices")

        elif request.POST.get('choice'):
            active = 'active_wait'

        # else:
        #     return redirect("player_choices")

        # render(request, "trivia/player_choices", active_view)
        # return redirect("player_choices")
    else:

        if request.session['player_choice']:

            cq = CurrentQuestion.objects.get(q=1)
            # q = Question.objects.get(id=cq.question)
            correct_answer = cq.question.correct_choice

            if request.session['player_choice'] == correct_answer:
                active = 'active_correct'
            else:
                active = 'active_incorrect'

    # return render(request, "trivia/player_choices.html")
    active_view = {
        'active': active
    }
    return render(request, "trivia/player_choices.html", active_view)


