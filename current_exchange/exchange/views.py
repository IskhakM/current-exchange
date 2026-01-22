from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CurrenceRate
from .serializer import CurrencyRateSerializer
from .services import get_current_usd_rate
from .constants import LIMIT


class CurrencyRateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CurrenceRate.objects.all()
    serializer_class = CurrencyRateSerializer

    def list(self, request, *args, **kwargs):
        current_rate = get_current_usd_rate()

        history = CurrenceRate.objects.all()[:LIMIT]
        serializer = self.get_serializer(history, many=True)

        if not current_rate and not history.exists():
            return Response(
                {'error':
                 'Нет информации о курсе валюты. Возможно проблема с API'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        response_data = {
            'usd_current': current_rate.rate if current_rate else None,
            'latest_10_requests': serializer.data,
        }

        return Response(response_data)
