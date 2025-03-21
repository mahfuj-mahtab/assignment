# Generated by Django 5.1.7 on 2025-03-21 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicineapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('OUTOFSTOCK', 'Out of Stock')], max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='medicine_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicineapp.medicine'),
        ),
    ]
