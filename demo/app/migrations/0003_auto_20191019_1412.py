# Generated by Django 2.2.6 on 2019-10-19 14:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20191019_1411'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='step',
            unique_together={('User', 'Date')},
        ),
    ]