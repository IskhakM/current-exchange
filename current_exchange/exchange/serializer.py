from rest_framework import serializers
from .models import CurrenceRate


class CurrencyRateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CurrenceRate
        fields = ('rate', 'created_at')
