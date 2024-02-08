from django.db import models


# Create your models here.
class Shooter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShooterGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Shooter, related_name='shootergame', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    release = models.DateTimeField('Release Date')
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def release_date(self):
        return self.release


class RPG(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RPGGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(RPG, related_name='rpggame', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    release = models.DateTimeField('Release Date')
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def release_date(self):
        return self.release


class Sports(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SportsGame(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Sports, related_name='sportsgame', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    release = models.DateTimeField('Release Date')
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def release_date(self):
        return self.release
