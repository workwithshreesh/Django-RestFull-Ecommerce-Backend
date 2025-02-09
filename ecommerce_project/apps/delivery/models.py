from django.db import models
from ..orders.models import Orders

# Column Name	Data Type	Description
# id	Primary Key	Unique delivery ID
# order_id	Foreign Key	Reference to Orders
# address	Text	Delivery address
# delivery_type	Enum	Free/Charged
# delivery_cost	Decimal	Cost of delivery
# expected_date	Date	Expected delivery date

class Delivery(models.Model):
    order = models.OneToOneField(Orders, on_delete=models.CASCADE)
    delivery_address = models.TextField()
    delivery_date = models.DateField()
    delivery_status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ])
    delivery_charge = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

    def __str__(self):
        return f"Delivery for Order {self.order.id} - Status: {self.delivery_status}"
