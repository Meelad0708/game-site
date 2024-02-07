from django.db import models
import datetime
# Create your models here.
class Shooter(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ShooterGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Shooter, on_delete=models.CASCADE)
    release = models.DateTimeField('Release Date')
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.title and self.release