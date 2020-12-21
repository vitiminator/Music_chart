from rest_framework import serializers

from .models import Musician


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['author', 'song', 'position']