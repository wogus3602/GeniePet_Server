from django.shortcuts import render
from .models import feed
from .serializers import FeedSerializer
from rest_framework import viewsets
# Create your views here.

class FeedViewSet(viewsets.ModelViewSet):
    queryset = feed.objects.all()
    serializer_class = FeedSerializer
