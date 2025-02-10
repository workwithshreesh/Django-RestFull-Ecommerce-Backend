from django.db import models
from products.models import Products

# Column Name	Data Type	Description
# id	Primary Key	Unique inventory ID
# product_id	Foreign Key	Reference to Products
# stock_quantity	Integer	Available stock quantity
# restock_date	Date	Last restock date

class Inventory(models.Model):
    Inventory_Id = models.AutoField(primary_key=True,null=False)
    Product_Id = models.ForeignKey(Products,null=False, on_delete=models.CASCADE)
    Stock_Quantity = models.IntegerField(null=False)
    Restock_Date = models.DateTimeField(auto_now_add=True)