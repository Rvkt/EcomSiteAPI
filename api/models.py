from django.db import models

class Product(models.Model):
    """
    Product Model

    This model represents a product in the EcomSiteAPI. It stores essential information about each product.

    Fields:
        name (str): The name of the product (up to 200 characters).
        description (text): A detailed description of the product.
        price (Decimal): The price of the product with a maximum of 10 digits and 2 decimal places.
        quantity (int): The available quantity of the product (must be a positive integer).
        category (str): The category to which the product belongs (up to 20 characters).

        created_date (datetime): The date and time when the product was created (auto-generated).
        updated_date (datetime): The date and time of the last update to the product (auto-updated).

    Meta:
        verbose_name (str): Singular name for the model (Product).
        verbose_name_plural (str): Plural name for the model (Products).

    Methods:
        __str__(): Provides a human-readable representation of the product, returning its name.

    Usage:
        Use this model to define and store product information in the EcomSiteAPI database.
    """

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=20)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
