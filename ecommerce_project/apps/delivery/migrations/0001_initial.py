# Generated by Django 5.1.6 on 2025-02-10 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Delivery",
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
                ("delivery_address", models.TextField()),
                ("delivery_date", models.DateField()),
                (
                    "delivery_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("shipped", "Shipped"),
                            ("delivered", "Delivered"),
                            ("cancelled", "Cancelled"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "delivery_charge",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
                ),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
            ],
            options={
                "verbose_name": "Delivery",
                "verbose_name_plural": "Deliveries",
            },
        ),
    ]
