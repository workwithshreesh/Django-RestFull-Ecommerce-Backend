from django.db import models
from django.contrib.auth import get_user_model
from products.models import Products

# Cart Table
# Column Name	Data Type	Description
# id	Primary Key	Unique cart ID
# user_id	Foreign Key	Reference to Users
# created_at	DateTime	Cart creation time
# is_active	Boolean	Indicates if the cart is active


class Cart(models.Model):
    Cart_Id = models.AutoField(primary_key=True)  
    User_Id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
    Created_At = models.DateTimeField(auto_now_add=True)
    Is_Active = models.BooleanField(default=True)



# CartItem
# Column Name	Data Type	Description
# id	Primary Key	Unique cart item ID
# cart_id	Foreign Key	Reference to Cart
# product_id	Foreign Key	Reference to Products
# quantity	Integer	Number of units added
# price	Decimal	Price at the time of addition
# added_at	DateTime	Timestamp for adding product


class CartItem(models.Model):
    CartItem_Id = models.AutoField(primary_key=True)
    Cart_Id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(Products, on_delete=models.CASCADE)  # Fix the incorrect Cart reference
    Cart_Quantity = models.PositiveIntegerField()  # Ensures quantity is always positive
    Cart_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Added_At = models.DateTimeField(auto_now=True)  # Captures update timestamp



