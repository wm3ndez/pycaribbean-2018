import names
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils.text import slugify


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--quantity', type=int)

    def handle(self, *args, **options):
        quantity = options.get('quantity')
        users = []
        for i in range(quantity):
            name = names.get_full_name()
            username = slugify(name)

            users.append(User(
                email='%s@example.com' % username,
                username=username,
                first_name=name.split(' ')[0],
                last_name=name.split(' ')[1]
            ))

        User.objects.bulk_create(users)

