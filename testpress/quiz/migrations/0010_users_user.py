# Generated by Django 2.2 on 2020-11-05 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0009_auto_20201105_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user',
            field=models.OneToOneField(default='no user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]