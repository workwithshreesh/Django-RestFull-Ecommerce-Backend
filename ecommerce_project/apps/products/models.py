from django.db import models

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
    Category_Id = models.AutoField(primary_key=True, null=True)
    Category_Name = models.CharField(max_length=255)
    Created_At = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    Product_Id = models.AutoField(primary_key=True, null=False)
    Product_Name = models.CharField(max_length=255, null=False)
    Product_Description = models.TextField(null=False)
    Product_Price = models.DecimalField(max_digits=10, null=False)
    Product_Stock_Quantity = models.IntegerField(null=False)
    Category_Id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    Created_At = models.DateTimeField(auto_now_add=True)
    

# WishList
# Column Name	Data Type	Description
# id	Primary Key	Unique wishlist ID
# user_id	Foreign Key	Reference to Users
# product_id	Foreign Key	Reference to Products
# created_at	DateTime	Wishlist creation time



# Returned Products Management Table (Seller Return Tracking)
# Column Name	Data Type	Description
# return_entry_id	INT (PK)	Unique Return Entry ID
# return_request_id	INT (FK)	Reference to the Return Request
# product_id	INT (FK)	Reference to the product
# return_status	ENUM('pending', 'in_transit', 'received', 'damaged')	Product return status
# seller_confirmation	BOOLEAN	Seller confirmation for receipt
# return_quantity	INT	Number of products returned
# return_remarks	TEXT	Seller remarks on the returned product
# confirmed_at	TIMESTAMP	Seller confirmation timestamp



    