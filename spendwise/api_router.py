from rest_framework import routers

from spendwise.core.api.views import CategoryViewSet, ExpenseViewSet


router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"expenses", ExpenseViewSet)
