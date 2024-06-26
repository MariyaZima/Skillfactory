# Generated by Django 5.0.2 on 2024-04-17 18:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_rename_many_to_many_relation_post_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
