from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import include, url

router = DefaultRouter()
router.register('feed', views.FeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
	]