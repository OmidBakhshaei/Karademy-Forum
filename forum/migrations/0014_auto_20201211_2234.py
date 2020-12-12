# Generated by Django 3.1.3 on 2020-12-11 19:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0013_auto_20201211_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]