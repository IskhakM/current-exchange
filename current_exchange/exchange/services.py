from decimal import Decimal

import requests
from django.conf import settings
from django.utils import timezone

from .models import CurrenceRate
from .constants import INTERVAL


def get_current_usd_rate():
    last_rate = CurrenceRate.objects.first()

    new_record = not last_rate or _is_expired(last_rate)

    if new_record:
        return CurrenceRate.objects.create(rate=_get_rate_from_api())


def _is_expired(rate: CurrenceRate) -> bool:
    return timezone.now() - rate.created_at > INTERVAL


def _get_rate_from_api() -> Decimal:
    response = requests.get(settings.CBR_API_URL, timeout=5)
    response.raise_for_status()
    data = response.json()
    return Decimal(str(data['Valute']['USD']['Value']))
