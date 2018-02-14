# Generated by Django 2.0.1 on 2018-02-14 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('approved', models.BooleanField(db_index=True, default=False)),
                ('featured', models.BooleanField(db_index=True, default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='b3_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='b3_posts', to='main.Category')),
                ('tags', models.ManyToManyField(related_name='b3_posts', to='main.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(db_index=True, default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog3.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='b3_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]