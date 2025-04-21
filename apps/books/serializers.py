from rest_framework import serializers
from .models import Author, Book, Rental, Penalty, ActionHistory
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Rental
        fields = '__all__'


class PenaltySerializer(serializers.ModelSerializer):
    rental = RentalSerializer(read_only=True)

    class Meta:
        model = Penalty
        fields = '__all__'


class ActionHistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = ActionHistory
        fields = '__all__'
