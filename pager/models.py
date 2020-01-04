from django.db import models

# Create your models here.


class Device(models.Model):
    nick = models.CharField(max_length=20)
    capcode = models.CharField(max_length=21)
