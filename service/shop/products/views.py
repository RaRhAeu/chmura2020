from rest_framework.viewsets import ModelViewSet
from shop.products.models import Product
from shop.products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('-created')
    serializer_class = ProductSerializer
