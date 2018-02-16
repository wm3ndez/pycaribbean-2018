import random
from importlib import import_module

import loremipsum
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from blog.main.models import Tag, Category


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--blog', type=int)
        parser.add_argument('--quantity', type=int)

    def handle(self, *args, **options):
        blog = options.get('blog')
        quantity = options.get('quantity')
        blog_models = import_module('blog.blog%s.models' % blog)
        Post = blog_models.Post

        users = list(User.objects.all())
        categories = list(Category.objects.all())

        posts = []
        for i in range(int(quantity)):
            amount = int(random.random() * 4) + 1
            content = ' '.join(loremipsum.get_paragraphs(amount, True))
            title = loremipsum.generate_sentence(True)[2]
            posts.append(
                Post.objects.create(
                    author=random.choice(users),
                    category=random.choice(categories),
                    title=title[:60],
                    content=content,
                    approved=random.random() < 0.8,  # ~80% post approved
                    featured=random.random() < 0.1  # ~10% post approved
                )
            )

        tags = list(Tag.objects.all())

        for post in posts:
            for i in range(int(random.random() * 4)):
                comment = loremipsum.get_paragraph(True)
                blog_models.PostComment.objects.create(
                    post=post,
                    user=random.choice(users),
                    comment=comment,
                    approved=random.random() < 0.8  # ~80% post approved
                )

            for tag in random.choices(tags, k=random.choice([2, 3, 4])):
                post.tags.add(tag)
