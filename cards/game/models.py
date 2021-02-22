from django.db import models

# Create your models here.


class BlackCard(models.Model):
    text = models.TextField()
    pick = models.IntegerField()
    draw = models.IntegerField()

class WhiteCard(models.Model):
    text = models.TextField()