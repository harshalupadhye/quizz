# Generated by Django 2.2 on 2020-11-06 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0019_quizzquestion_studentans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizzquestion',
            name='studentAns',
        ),
    ]
