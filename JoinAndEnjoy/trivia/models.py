from django.db import models
from django.urls import reverse


class Player(models.Model):
    # id_player=models.IntegerField(default=0)
    name = models.CharField(max_length=200)

    # score= models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Player:detail", args=(self.id,))


class Question(models.Model):
    question = models.TextField(max_length=200)
    choice_1 = models.TextField(max_length=200)
    choice_2 = models.TextField(max_length=200)
    choice_3 = models.TextField(max_length=200)
    choice_4 = models.TextField(max_length=200)
    correct_choice = models.IntegerField()


class CurrentQuestion(models.Model):
    q = models.IntegerField(default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answering_end = models.DateTimeField('date published')
    display_end = models.DateTimeField('date published')

class helper(models.Model):
    i = models.IntegerField(default=1)
    first_time = models.IntegerField(default=0)
    second_time = models.IntegerField(default=0)

