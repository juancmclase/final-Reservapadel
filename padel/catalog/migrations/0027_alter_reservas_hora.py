# Generated by Django 3.2.9 on 2022-06-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20220605_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='hora',
            field=models.CharField(choices=[['17:00', '17:00'], ['18:30', '18:30'], ['20:00', '20:00'], ['21:30', '21:30']], max_length=20, null=True),
        ),
    ]
