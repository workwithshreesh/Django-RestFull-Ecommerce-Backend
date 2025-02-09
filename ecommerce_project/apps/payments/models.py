from django.db import models
from ..orders.models import Orders

# Column Name	Data Type	Description
# id	Primary Key	Unique payment ID
# order_id	Foreign Key	Reference to Orders
# payment_mode	Enum	Credit Card/Debit Card/COD
# payment_status	Enum	Successful/Pending/Failed
# payment_date	DateTime	Payment timestamp

class Payments(models.Model):
    Payment_Id = models.AutoField(primary_key=True, null=False)
    Order_Id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    Payment_Mode = models.CharField(max_length=20, choices=[
        ("Card/Credit","Credit Card"),
        ("Card/Debit","Card Debit"),
        ("COD","COD"),
        ("UPI","UPI")
    ])
    Payment_Status = models.CharField(choices=[
        ("Successful","Successful"),
        ("Pending","Pending"),
        ("Failed","Failed")
    ])
    Payment_Date = models.DateTimeField(auto_now_add=True)
    
