# Generated by Django 2.2 on 2020-11-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.IntegerField(default=0)),
                ('ans', models.CharField(max_length=20)),
            ],
        ),
    ]
