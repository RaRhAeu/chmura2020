from rest_framework.serializers import HyperlinkedModelSerializer
from shop.products.models import Product


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
