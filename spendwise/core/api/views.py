from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_filters import rest_framework as filters

from .serializers import CategorySerializer, ExpenseSerializer, ExpenseReadSerializer
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
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ExpenseReadSerializer
        return ExpenseSerializer    

    def get_queryset(self):
        return super().get_queryset().order_by("-date")
