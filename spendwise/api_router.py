from rest_framework import routers

from spendwise.core.api.views import CategoryViewSet


router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
