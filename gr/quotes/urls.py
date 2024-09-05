# quotes/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet, AuthorViewSet, BookViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
