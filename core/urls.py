from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(prefix='books', viewset=views.BookViewSet, basename='book')
router.register(prefix='authors', viewset=views.AuthorViewSet, basename='author')


urlpatterns = router.urls