from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import include, url
from keras.models import load_model
router = DefaultRouter()
router.register('feed', views.FeedViewSet)
router.register('dog', views.DogViewSet)
router.register('rank', views.RankViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('pot/upload/',views.post),
	]