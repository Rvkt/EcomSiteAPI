from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('products/', views.products, name='products'),
    path('product-detail/<str:pk>/', views.productDetail, name='productDetail'),
    path('product-create/', views.productCreate, name='productCreate'),
    path('product-update/<str:pk>/', views.productUpdate, name='productUpdate'),
    path('product-delete/<str:pk>/', views.productDelete, name='productDelete'),
]
