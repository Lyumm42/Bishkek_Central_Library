from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    is_active = models.BooleanField(default=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def is_available(self):
        return self.available_copies > 0


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rented_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} rented {self.book}"

    def is_overdue(self):
        return self.return_date is None and timezone.now() > self.due_date


class Penalty(models.Model):
    rental = models.OneToOneField(Rental, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Penalty for {self.rental} - {self.amount}₸"


class ActionHistory(models.Model):
    ACTION_CHOICES = [
        ('RENT', 'Book rented'),
        ('RETURN', 'Book returned'),
        ('PENALTY', 'Penalty applied'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=7, choices=ACTION_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.get_action_display()} - {self.book} on {self.timestamp}"
