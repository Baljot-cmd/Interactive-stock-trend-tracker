from reset_framework import serializers
from .models import PriceData


class PriceDataSerializer(serializers.ModelSerializers):
    class Meta:
        Model = PriceData
        fields = ['ticker','price','timestamp']