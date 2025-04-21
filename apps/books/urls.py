from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, RentalViewSet, PenaltyViewSet, ActionHistoryViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'rentals', RentalViewSet)
router.register(r'penalties', PenaltyViewSet)
router.register(r'history', ActionHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
