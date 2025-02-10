from django.db import models
from django.contrib.auth import get_user_model
from orders.models import OrderItem
from products.models import Products




class ReturnedRequestProduct(models.Model):
    Return_Request_Id = models.AutoField(primary_key=True)
    Return_Request_Id = models.ForeignKey(get_user_model(),limit_choices_to={"role":"User"}, on_delete=models.CASCADE)
    Order_Item_Id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(Products,on_delete=models.CASCADE)
    Return_Reason = models.TextField()
    Return_Status = models.CharField(max_length=20)
    Requested_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)




class ReturnProducts(models.Model):
    Return_Entry_Id = models.AutoField(primary_key=True, null=False)
    Return_Request_Id = models.ForeignKey(ReturnedRequestProduct, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(Products,on_delete=models.CASCADE)
    Return_Status = models.CharField(max_length=30)
    Seller_Confirmation = models.BooleanField(null=False)
    Return_Quantity = models.IntegerField(null=False)
    Return_Remark = models.TextField()
    Confirmed_At = models.DateTimeField(auto_now_add=True)



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



# Column Name	Data Type	Description
# return_request_id	INT (PK)	Unique Return Request ID
# customer_id	INT (FK)	Reference to the customer
# order_item_id	INT (FK)	Reference to the specific order item
# product_id	INT (FK)	Reference to the product being returned
# return_reason	TEXT	Customer's reason for the return
# return_status	ENUM('requested', 'approved', 'rejected', 'completed')	Return request status
# requested_at	TIMESTAMP	Return request date
# updated_at	TIMESTAMP	Last update timestamp