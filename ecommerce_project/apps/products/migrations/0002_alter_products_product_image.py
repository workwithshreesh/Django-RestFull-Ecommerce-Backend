# Generated by Django 5.1.6 on 2025-02-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="Product_Image",
            field=models.ImageField(
                default="products/default.jpg", upload_to="static/product_images/"
            ),
            preserve_default=False,
        ),
    ]
