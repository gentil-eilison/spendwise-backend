from django.db.models import QuerySet


class ExpenseQuerySet(QuerySet):
    def total_amount(self):
        expenses_values = list(self.values_list("value", flat=True))
        return sum(expenses_values)