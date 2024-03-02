from django.db import models
import djmoney.models.fields as djm_models

from .managers import ExpenseQuerySet


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name}"


class Expense(models.Model):
    date = models.DateField(verbose_name="Date")
    value = djm_models.MoneyField(
        max_digits=19, 
        decimal_places=2,
        verbose_name="Value",
        default_currency="BRL"
    )
    description = models.CharField(max_length=128, verbose_name="Description")
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="expenses", verbose_name="Category")

    objects = ExpenseQuerySet.as_manager()

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
    
    def __str__(self):
        return f"{self.description} - {self.value} at {self.date}"
