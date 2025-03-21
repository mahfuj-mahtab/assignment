# Generated by Django 5.1.7 on 2025-03-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=100)),
                ("customer_phone", models.CharField(max_length=10)),
                ("customer_address", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "ADMIN"),
                    ("MEDICINEMANAGER", "MEDICINEMANAGER"),
                    ("ORDERMANAGER", "ORDERMANAGER"),
                    ("CUSTOMER", "CUSTOMER"),
                ],
                max_length=30,
            ),
        ),
    ]
