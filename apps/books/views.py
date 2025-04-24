from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Author, Book, Rental, Penalty, ActionHistory
from .serializers import AuthorSerializer, BookSerializer, RentalSerializer, PenaltySerializer, ActionHistorySerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'available_copies']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'available_copies']


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RentalListCreateView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class RentalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class PenaltyListCreateView(generics.ListCreateAPIView):
    queryset = Penalty.objects.all()
    serializer_class = PenaltySerializer


class PenaltyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Penalty.objects.all()
    serializer_class = PenaltySerializer


class ActionHistoryListView(generics.ListAPIView):
    queryset = ActionHistory.objects.all()
    serializer_class = ActionHistorySerializer
