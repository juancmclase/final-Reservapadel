# Generated by Django 3.2.9 on 2022-05-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20211208_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='hora1',
            field=models.IntegerField(choices=[[0, '17:00'], [1, '18:30'], [2, '20:00'], [3, '21:30']], null=True),
        ),
    ]
