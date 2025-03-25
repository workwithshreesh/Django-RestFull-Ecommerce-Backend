from django.db import models
from django.contrib.auth import get_user_model
from products.models import Products

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

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        COMPLETED = 'Completed', 'Completed'
        CANCELED = 'Canceled', 'Canceled'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

    def __str__(self):
        return f"Item {self.product.name} in Order {self.order.id}"

    

    
    