from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Product
from api.serializer import ProductSerializer

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

    
@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)

    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Item successfully deleted!')
