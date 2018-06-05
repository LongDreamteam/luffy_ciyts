from luffy import models
from rest_framework import serializers

class PricePolicyModelSerializer(serializers.ModelSerializer):
    period = serializers.CharField(source='get_valid_period_display')
    class Meta:
        model = models.PricePolicy
        fields = ['id', 'valid_period', 'price', 'period']
