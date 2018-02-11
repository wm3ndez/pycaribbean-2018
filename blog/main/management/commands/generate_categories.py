import random

import names
from django.core.management import BaseCommand

from blog.main.models import Category


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--quantity', type=int)

    def handle(self, *args, **options):
        quantity = options.get('quantity')
        for i in range(quantity):
            category = Category.objects.create(
                name=names.get_last_name()
            )

            if random.random() < .33:
                parent_id = random.choice(list(range(1, Category.objects.count())))
                category.parent_id = parent_id
                category.save()
