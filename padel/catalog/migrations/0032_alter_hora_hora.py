# Generated by Django 3.2.9 on 2022-06-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0031_auto_20220606_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hora',
            name='hora',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
