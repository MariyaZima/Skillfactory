# Generated by Django 5.0.2 on 2024-04-09 18:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_one_to_many_relation_comment_comment_post_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]