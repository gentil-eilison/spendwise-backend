from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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

    @action(("GET", ), detail=False, url_path="total-amount")
    def total_amount(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        total_amount = filtered_queryset.total_amount()
        return Response(data={"total_amount": total_amount}, status=status.HTTP_200_OK)