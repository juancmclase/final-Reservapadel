# Generated by Django 3.2.9 on 2021-12-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_pistas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pistas',
            name='codigo',
            field=models.CharField(max_length=50),
        ),
    ]
