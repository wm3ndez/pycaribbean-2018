import random

import loremipsum
from django.core.management import BaseCommand

from blog.main.models import Tag


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--quantity', type=int)

    def handle(self, *args, **options):
        quantity = options.get('quantity')
        for i in range(quantity):
            sentence = loremipsum.generate_sentence(True)[2]
            sentence = sentence.split(' ')

            # tags with 3 words or fewer
            tag = ' '.join(sentence[:int(random.random() * 3) + 1])
            Tag.objects.create(tag=tag)
