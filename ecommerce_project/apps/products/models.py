from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# id	Primary Key	Unique product ID
# name	String	Product name
# description	Text	Product details
# price	Decimal	Product price
# stock_quantity	Integer	Quantity in stock
# category_id	Foreign Key	Category reference
# created_at	DateTime	Creation timestamp


# Column Name	Data Type	Description
# id	Primary Key	Unique category ID
# name	String	Name of the category
# created_at	DateTime	Creation timestamp


class ProductCategory(models.Model):
    Category_Id = models.AutoField(primary_key=True)
    Category_Name = models.CharField(max_length=255)
    Created_At = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Products(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=255, null=False)
    Product_Description = models.TextField(null=False)
    Product_Price = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    Product_Stock_Quantity = models.IntegerField(null=False)
    Product_Image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    Category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    Created_At = models.DateTimeField(auto_now_add=True)

    # Seller Integration
    Seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'SELLER'}
    )
    Is_Active = models.BooleanField(default=False)  # Product listing status

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    

# WishList
# Column Name	Data Type	Description
# id	Primary Key	Unique wishlist ID
# user_id	Foreign Key	Reference to Users
# product_id	Foreign Key	Reference to Products
# created_at	DateTime	Wishlist creation time


class WishList(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), null=False, on_delete=models.CASCADE, related_name="wishlist_items")
    product = models.ForeignKey(Products, null=False, on_delete=models.CASCADE, related_name="wishlists")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "products"  # Ensure the app name matches the structure.
        unique_together = ('user', 'product')
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"





    