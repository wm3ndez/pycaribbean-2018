from importlib import import_module

from django.core.management import BaseCommand

from blog.blog1 import models as b1_models


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--blog', type=int)

    def handle(self, *args, **options):
        blog = options.get('blog')
        target_models = import_module('blog.blog%s.models' % blog)

        for post in b1_models.Post.objects.all():
            _post = target_models.Post.objects.create(
                category=post.category,
                title=post.title,
                content=post.content,
                author=post.author,
                date=post.date,
                published=post.published,
                approved=post.approved,
                featured=post.featured,
            )

            for tag in post.tags.all():
                _post.tags.add(tag)
