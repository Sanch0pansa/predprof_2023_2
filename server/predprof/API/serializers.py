from rest_framework import serializers
from API.models import Day


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'
