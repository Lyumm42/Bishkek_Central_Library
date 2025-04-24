from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view()),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view()),

    path('books/', views.BookListCreateView.as_view()),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view()),

    path('rentals/', views.RentalListCreateView.as_view()),
    path('rentals/<int:pk>/', views.RentalRetrieveUpdateDestroyView.as_view()),

    path('penalties/', views.PenaltyListCreateView.as_view()),
    path('penalties/<int:pk>/', views.PenaltyRetrieveUpdateDestroyView.as_view()),

    path('actions/', views.ActionHistoryListView.as_view()),
]
