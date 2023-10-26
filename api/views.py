from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'products/',
        'Detail View': 'product-detail/<str:pk>/',
        'Create': 'product-create/',
        'Update': 'product-update/<str:pk>/',
        'Delete': 'product-delete/<str:pk>/',
    }
    return Response(api_urls)