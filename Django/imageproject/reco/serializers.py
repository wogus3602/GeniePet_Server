from .models import Feed,Dog,Review
from rest_framework import serializers

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['id','name', 'price','text','image']



class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['name', 'age','species']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['feed', 'pub_date', 'user_name', 'comment' ,'rating']