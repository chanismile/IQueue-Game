from django import forms
from django.shortcuts import render



# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = "__all__"
from trivia.models import Player


def main_screen(request):
    return render(request, "trivia/main_screen.html")

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


def player_welcome(request):
    if request.method == "POST":
         form = ExpenseForm(request.POST)
         # assert False, form.cleaned_data
         if form.is_valid():
             form.instance.save()

        # Player.objects.create(name=request.POST['player_name'],
        #                     score=0)
            # return redirect(form.instance)
    # return render(request, "trivia/player_welcome.html")
    else:
        form = ExpenseForm()
    return render(request, "trivia/player_welcome.html", {
        'form': form,
    })

def player_answers(request):
    return render(request, "trivia/player_answers.html")

