# Generated by Django 2.2 on 2020-11-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20201105_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.IntegerField()),
                ('ans', models.CharField(max_length=20)),
            ],
        ),
    ]