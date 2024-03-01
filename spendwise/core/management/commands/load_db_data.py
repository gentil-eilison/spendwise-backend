from django.core.management.base import BaseCommand

from spendwise.core.models import Category


class Command(BaseCommand):
    help = "Creates categories"

    def handle(self, *args, **kwargs):
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
