from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import Author, Book
from core.serializers import AuthorSerializer, BookSerializer
# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

