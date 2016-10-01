from halls.views import HallsViewSet, ContentHallViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'details', HallsViewSet)
router.register(r'contents', ContentHallViewSet)
