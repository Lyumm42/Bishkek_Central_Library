from django.contrib import admin
from .models import Author, Book, Rental, Penalty, ActionHistory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
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
    list_display = ('user', 'book',  )

    search_fields = ('user__username', 'book__title')



@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('amount',)
    search_fields = ('user__username',)


@admin.register(ActionHistory)
class ActionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'action')
    readonly_fields = ('timestamp',)
