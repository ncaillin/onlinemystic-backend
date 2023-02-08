from django.urls import path
from .views import homePageView, getReadingFromCards

urlpatterns = [
    path("", homePageView, name='home'),
    path("given-cards", getReadingFromCards, name="given_cards")
]
