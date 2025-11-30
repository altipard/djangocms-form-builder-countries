"""URL configuration for tests."""

from django.urls import path, include

urlpatterns = [
    path('', include('cms.urls')),
]
