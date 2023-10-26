from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Product model.

    This serializer provides a representation of the Product model with a hyperlinked detail view.

    Attributes:
        product_detail: A hyperlinked identity field for accessing a detailed view of the product.

    Meta:
        - model: The Product model.
        - fields: All fields from the Product model.

    Usage:
        This serializer is used to represent and manipulate Product objects, including access to a detailed view.
    """

    product_detail = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Product
        fields = '__all__'
