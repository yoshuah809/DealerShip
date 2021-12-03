# Generated by Django 3.2.9 on 2021-12-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20211202_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_sold',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(choices=[('Gas', 'Gas'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], default='Gas', max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='number_of_doors',
            field=models.CharField(choices=[('2', '2'), ('4', '4'), ('6', '6')], default=4, max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='rowseat',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=2),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], default='Automatic', max_length=20),
        ),
    ]
