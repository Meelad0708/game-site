from django.contrib import admin
from .models import Shooter, ShooterGame, RPG, RPGGame, Sports, SportsGame
# Register your models here.
admin.site.register(Shooter)
admin.site.register(ShooterGame)
admin.site.register(RPG)
admin.site.register(RPGGame)
admin.site.register(Sports)
admin.site.register(SportsGame)