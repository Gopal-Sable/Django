# artistapp/urls.py

from django.urls import path
from .views import WorkListCreateView, ArtistFilterListView, ArtistRegistrationView

urlpatterns = [
    path('works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('artists/', ArtistFilterListView.as_view(), name='artist-filter-list'),
    path('register/', ArtistRegistrationView.as_view(), name='artist-registration'),
]
