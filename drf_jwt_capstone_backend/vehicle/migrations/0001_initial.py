# Generated by Django 3.2.8 on 2021-12-03 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VIN', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('mfr', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('main_image', models.ImageField(upload_to='images')),
                ('purchased_date', models.DateField()),
                ('date_sold', models.DateField(blank=True, null=True)),
                ('features', models.CharField(max_length=100)),
                ('number_of_doors', models.IntegerField(choices=[(2, 2), (4, 4), (6, 6)], default=4)),
                ('rowseat', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=2)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], default='Automatic', max_length=20)),
                ('fuel_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vehicle.fuel_type')),
                ('vehicle_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vehicle.vehicle_type')),
            ],
        ),
    ]
