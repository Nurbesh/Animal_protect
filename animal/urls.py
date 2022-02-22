from django.urls import path, include
from rest_framework import routers
from .views import AnimalView

router = routers.DefaultRouter()
router.register('animal', AnimalView)

urlpatterns = [
    path('', include(router.urls))
]