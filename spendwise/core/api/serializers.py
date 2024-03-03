from rest_framework import serializers

from ..models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ("id", "date", "value", "description", "category")


class ExpenseReadSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    currency = serializers.CharField(source="value.currency", read_only=True)

    class Meta:
        model = Expense
        fields = ("id", "date", "value", "description", "category", "currency")

