from django.db import models
from django.contrib.auth import get_user_model

# Column Name	Data Type	Description
# id	Primary Key	Unique order ID
# user_id	Foreign Key	Reference to Users
# status	Enum	Pending/Completed/Canceled
# total_price	Decimal	Total order price
# created_at	DateTime	Order creation timestamp


# Column Name	Data Type	Description
# id	Primary Key	Unique order item ID
# order_id	Foreign Key	Reference to Orders
# product_id	Foreign Key	Reference to Products
# quantity	Integer	Quantity of the product
# price	Decimal	Price at the time of purchase

User = get_user_model()

class Orders(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        COMPLETED = 'Completed', 'Completed'
        CANCELED = 'Canceled', 'Canceled'
    Order_Id = models.AutoField(primary_key=True, null=True)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Order_Status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    Order_Total_Price = models.DecimalField(max_digits=10)
    Created_At = models.DateTimeField(auto_now_add=True)
    

class OrderItems(models.Model):
    OrderItem_Id = models.AutoField(primary_key=True, null=False)
    Order_Id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(on_delete=models.CASCADE)
    OrderItem_Quantity = models.IntegerField(null=False)
    OrderItem_Price = models.DecimalField(max_digits=10)
    

    
    