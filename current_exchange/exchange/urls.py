from django.urls import path, include
from rest_framework import routers

from .views import CurrencyRateViewSet

router = routers.DefaultRouter()
router.register('get-current-usd', CurrencyRateViewSet, basename='current_usd')

urlpatterns = [
    path('', include(router.urls))
]
