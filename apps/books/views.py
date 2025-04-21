from rest_framework import viewsets
from .models import Author, Book, Rental, Penalty, ActionHistory
from .serializers import AuthorSerializer, BookSerializer, RentalSerializer, PenaltySerializer, ActionHistorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class PenaltyViewSet(viewsets.ModelViewSet):
    queryset = Penalty.objects.all()
    serializer_class = PenaltySerializer


class ActionHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActionHistory.objects.all()
    serializer_class = ActionHistorySerializer
