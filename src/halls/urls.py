from halls.views import HallsViewSet, ContentSubHallViewSet, SubHallsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'details', HallsViewSet)

router_sub_halls = routers.SimpleRouter()
router_sub_halls.register(r'details', SubHallsViewSet)
router_sub_halls.register(r'contents', ContentSubHallViewSet)
