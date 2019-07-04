from rest_framework import serializers

from .models import Count_data


class CountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count_data
        fields = ('date', 'livename','count')


