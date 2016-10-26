from category.views import CategoryViewSet, CategorySubHallsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'details', CategoryViewSet)
router.register(r'hall', CategorySubHallsViewSet)

