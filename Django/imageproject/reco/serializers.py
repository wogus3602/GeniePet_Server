from .models import feed,Dog,Rank
from rest_framework import serializers

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = feed
        fields = ['id','name', 'price']



class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'age','species']

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['date','dog', 'value']