# Generated by Django 3.1.3 on 2020-12-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default='Python', max_length=30),
            preserve_default=False,
        ),
    ]
