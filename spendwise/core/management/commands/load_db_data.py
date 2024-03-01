from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.contrib.auth import get_user_model

from spendwise.core.models import Category


class Command(BaseCommand):
    help = "Creates categories"

    def create_superuser(self):
        User = get_user_model()
        try:
            User.objects.create_superuser(
                username="admin",
                password="spendwiseadmin@2024"
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Superuser already created"))
        
    def create_categories(self):
        categories_names = (
            "Housing",
            "Transportation",
            "Food",
            "Utilities",
            "Insurance",
            "Medial & Healthcare",
            "Saving",
            "Investing",
            "Debt Payment",
            "Personal Spending",
            "Entertainment",
            "Miscellaneous",
            "Other"
        )

        for name in categories_names:
            Category.objects.get_or_create(
                name=name
            )
        self.stdout.write(self.style.SUCCESS("Categories successfully created"))

    def handle(self, *args, **kwargs):
        self.create_categories()
        self.create_superuser()
