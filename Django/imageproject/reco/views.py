from django.shortcuts import render
from .models import feed,Dog,Rank
from .serializers import FeedSerializer,DogSerializer,RankSerializer
from rest_framework import viewsets
from keras.models import load_model
from PIL import Image
import numpy as np
import tensorflow as tf
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class FeedViewSet(viewsets.ModelViewSet):
    queryset = feed.objects.all()
    serializer_class = FeedSerializer
class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer

model = load_model('model.h5')
graph = tf.get_default_graph()

@csrf_exempt
def post(request):
    global graph
    with graph.as_default():
        test_image = request.FILES['model_pic']
        img = Image.open(test_image)
        img = img.convert("RGB")
        img = img.resize((224,224))
        data = np.asarray(img)
        X = np.array(data)
        X = X.astype("float") / 256
        X = X.reshape(-1, 224, 224,3)
        
        categories = ['GermanShepherd', 'GoldenRetriever', 'SiberianHusky']
        pred = model.predict(X)
        print(pred)
        result = [np.argmax(value) for value in pred]  
        print('New data category : ',categories[result[0]])
        return HttpResponse(categories[result[0]])