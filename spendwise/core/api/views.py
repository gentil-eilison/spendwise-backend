from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .serializers import CategorySerializer, ExpenseSerializer
from ..models import Category, Expense


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all().select_related("category")
