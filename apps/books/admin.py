from django.contrib import admin
from .models import Author, Book, Rental, Penalty, ActionHistory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available_copies')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')
    ordering = ('title',)


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rented_at', 'returned_at')
    list_filter = ('rented_at', 'returned_at')
    search_fields = ('user__username', 'book__title')
    date_hierarchy = 'rented_at'


@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'is_paid', 'issued_at')
    list_filter = ('is_paid',)
    search_fields = ('user__username',)
    date_hierarchy = 'issued_at'


@admin.register(ActionHistory)
class ActionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'action')
    readonly_fields = ('timestamp',)
