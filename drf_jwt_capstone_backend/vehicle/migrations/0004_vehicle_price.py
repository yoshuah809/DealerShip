# Generated by Django 3.2.8 on 2021-12-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicle_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=10000.0),
            preserve_default=False,
        ),
    ]
