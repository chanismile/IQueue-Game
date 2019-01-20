from django.shortcuts import render


def main_screen(request):
    return render(request, "trivia/main_screen.html")


def player_welcome(request):
    return render(request, "trivia/player_welcome.html")


def player_answers(request):
    return render(request, "trivia/player_answers.html")
