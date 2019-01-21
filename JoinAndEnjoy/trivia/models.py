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

class Questions(models.Model):
    question = models.TextField(max_length=200)
    choise_1 = models.TextField(max_length=200)
    choise_2 = models.TextField(max_length=200)
    choise_3 = models.TextField(max_length=200)
    choise_4 = models.TextField(max_length=200)
    the_choise = models.IntegerField()

class Answer(models.Model):
    question=models.IntegerField()
    num_answer=models.IntegerField()
    time_to_answer=models.DateTimeField('date published')
    time_to_despla_answer=models.DateTimeField('date published')

