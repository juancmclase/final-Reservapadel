# Generated by Django 3.2.9 on 2021-12-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20211206_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='horaf',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='horar',
            field=models.DateTimeField(),
        ),
    ]
