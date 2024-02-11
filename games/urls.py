from django.urls import path, include
from rest_framework import routers
from .views import ShooterViewSet, ShooterGameViewSet, RPGViewSet, RPGGameViewSet, SportsViewSet, SportsGameViewSet

router = routers.DefaultRouter()
router.register(r'shooters', ShooterViewSet)
router.register(r'shootergames', ShooterGameViewSet)
router.register(r'rpg', RPGViewSet)
router.register(r'rpggames', RPGGameViewSet)
router.register(r'sports', SportsViewSet)
router.register(r'sportsgames', SportsGameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]