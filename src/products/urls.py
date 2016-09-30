from .views import ProductsViewSet, ProductsHallsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'details', ProductsViewSet)
router.register(r'hall', ProductsHallsViewSet)

