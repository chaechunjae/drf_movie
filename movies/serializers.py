from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
