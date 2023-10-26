from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .models import Product
from .serializer import ProductSerializer

class WelcomeView(APIView):
    """
    Welcome to the EcomSiteAPI.

    For More Information, visit the provided link below.

    Attributes:
        None

    Methods:
        get(self, request): Retrieves and presents a welcome message with a link to access additional information.

    Usage:
        Access this view for a warm welcome and further details.
    """

    def get(self, request):
        message = "For More Information, visit the provided link:"
        api_url = reverse('api-root')  # You can adjust this URL name based on your project's URL configuration

        current_site = get_current_site(request)
        local_api_url = f"http://{current_site.domain}{api_url}"

        full_message = f"{message} {local_api_url}"
        return Response({'api': full_message})

class ProductViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Product objects.

    This viewset allows you to perform CRUD operations on Product objects.

    Attributes:
        queryset: The queryset of Product objects.
        serializer_class: The serializer class to use for Product objects.

    Methods:
        - product_detail(self, request, pk): Retrieves details of a specific Product.
        - product_delete(self, request, pk): Deletes a specific Product.

    Usage:
        Use this viewset to perform CRUD operations on Product objects.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['GET'])
    def product_detail(self, request, pk=None):
        """
        Retrieves details of a specific Product.

        This action retrieves and returns the details of a specific Product.

        Parameters:
            - request: The HTTP request object.
            - pk: The primary key of the Product to retrieve.

        Returns:
            JSON response containing the Product's details.

        Usage:
            Access this action to view the details of a specific Product.
        """
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def product_delete(self, request, pk=None):
        """
        Deletes a specific Product.

        This action deletes a specific Product and returns a success message.

        Parameters:
            - request: The HTTP request object.
            - pk: The primary key of the Product to delete.

        Returns:
            JSON response with a success message and a link to the product list.

        Usage:
            Access this action to delete a specific Product.
        """
        product = self.get_object()
        product.delete()
        response_data = {
            'message': 'Product deleted successfully',
            'back_url': '/products/'  # Specify the URL for the product list here
        }
        return Response(response_data)

