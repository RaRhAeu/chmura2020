from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.products.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
