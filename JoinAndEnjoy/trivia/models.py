from django.db import models

# Create your models here.
class Player(models.Model):
    # id_player=models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    # score= models.IntegerField(default=0)
