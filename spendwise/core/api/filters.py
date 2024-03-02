from django_filters import rest_framework as filters

from ..models import Expense


class ExpenseFilterSet(filters.FilterSet):
    class Meta:
        model = Expense
        fields = ("category", "date")
