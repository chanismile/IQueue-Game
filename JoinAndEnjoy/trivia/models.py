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