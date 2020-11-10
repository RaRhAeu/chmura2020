from rest_framework.serializers import ModelSerializer
from shop.products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
