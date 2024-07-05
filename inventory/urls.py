from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register('items', InventoryItemViewSet)
router.register('categories', CategoryViewSet)
router.register('suppliers',SupplierViewSet)
router.register('orders',PurchaseOrderViewSet)


urlpatterns = [
    
] +router.urls
