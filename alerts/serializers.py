from rest_framework import serializers
from .models import Alert, Route, PriceSnapshot


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class AlertSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Alert
        fields = ['id', 'target_price', 'is_active', 'user', 'route']


class PriceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSnapshot
        fields = '__all__'