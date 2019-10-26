from django.shortcuts import render
from .models import Feed,Dog,Review,Cart,Order
from .serializers import FeedSerializer,DogSerializer,ReviewSerializer,CartSerializer,OrderSerializer
from rest_framework import viewsets
from keras.models import load_model
from PIL import Image
import numpy as np
import tensorflow as tf
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
# Create your views here.

class FeedViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
class DogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
@csrf_exempt
def post(request):
    print(request.body)
    return JsonResponse('hi')