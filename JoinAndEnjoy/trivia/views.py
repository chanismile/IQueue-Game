from django.shortcuts import render, redirect


def main_screen(request):
    return render(request, "trivia/main_screen.html")


def player_welcome(request):
    if request.method == "POST":
        p = Player.objects.create(name=request.POST['name'])
        request.session['player_id'] = p.id
        return redirect('player_choices')

    return render(request, "trivia/player_welcome.html")


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

