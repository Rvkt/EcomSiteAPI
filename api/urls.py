from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, WelcomeView

# Create a router for the ProductViewSet
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    # URL for the welcome message view
    path('', WelcomeView.as_view(), name='api-welcome'),

    # URL patterns for API endpoints
    path('api/', include(router.urls), name='api-endpoints'),
]

"""
URL Configuration for the EcomSiteAPI

This URL configuration defines the endpoints for the EcomSiteAPI. It includes a welcome message and various API-related views.

Attributes:
    None

Usage:
    - Access the root URL to view the welcome message.
    - Access '/api/' to access the API endpoints provided by the ProductViewSet.
"""
