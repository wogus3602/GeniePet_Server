from .models import feed
from rest_framework import serializers

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = feed
        fields = ['id','name', 'price','rating']