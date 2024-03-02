from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_filters import rest_framework as filters

from .serializers import CategorySerializer, ExpenseSerializer
from ..models import Category, Expense
from .filters import ExpenseFilterSet


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all().select_related("category")
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = ExpenseFilterSet
