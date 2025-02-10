from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order
# 1. Billing Table
# Tracks customer billing information for completed orders.

# Column Name	Data Type	Description
# billing_id	INT (PK)	Unique billing record ID
# order_id	INT (FK)	Foreign key referencing orders.order_id
# customer_id	INT (FK)	Foreign key referencing users.user_id
# total_amount	DECIMAL(10, 2)	Total amount billed for the order
# billing_date	TIMESTAMP	Date of billing
# payment_method	ENUM('card', 'UPI', 'COD', 'wallet')	Payment method used
# payment_status	ENUM('pending', 'completed', 'failed')	Payment status
# delivery_charges	DECIMAL(10, 2)	Delivery charges (if any)
# discount_applied	DECIMAL(10, 2)	Discount amount applied
# final_amount	DECIMAL(10, 2)	Final amount after charges and discounts
# created_at	TIMESTAMP	Billing record creation date
# updated_at	TIMESTAMP	Last update of billing record
# 2. Payment Transactions Table
# Tracks individual payment transactions associated with orders and subscriptions.


class Billing(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='billing')
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='billing_info')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateTimeField(auto_now_add=True)
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Card'),
        ('UPI', 'UPI'),
        ('COD', 'Cash on Delivery'),
        ('wallet', 'Wallet')
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    delivery_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_applied = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Billing for Order #{self.order.order_id}"

    class Meta:
        db_table = 'billing'  




# Column Name	Data Type	Description
# transaction_id	INT (PK)	Unique payment transaction ID
# billing_id	INT (FK)	Foreign key referencing billing.billing_id
# transaction_amount	DECIMAL(10, 2)	Amount for this transaction
# transaction_date	TIMESTAMP	Date and time of transaction
# payment_status	ENUM('pending', 'completed', 'failed')	Transaction status
# payment_reference	VARCHAR(50)	Reference number from payment gateway
# payment_method	ENUM('card', 'UPI', 'wallet', 'net banking')	Payment method
# created_at	TIMESTAMP	Transaction record creation date
# updated_at	TIMESTAMP	Last update of transaction record
# 3. Invoice Table
# Stores detailed information for customer invoices.



class PaymentTransaction(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, related_name='transactions')
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    payment_reference = models.CharField(max_length=50)
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Card'),
        ('UPI', 'UPI'),
        ('wallet', 'Wallet'),
        ('net banking', 'Net Banking')
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.payment_reference} for Billing ID {self.billing.billing_id}"
    class Meta:
        db_table = 'payment_transactions' 




# Column Name	Data Type	Description
# invoice_id	INT (PK)	Unique invoice ID
# billing_id	INT (FK)	Foreign key referencing billing.billing_id
# invoice_number	VARCHAR(20)	Unique invoice number
# invoice_date	TIMESTAMP	Date of invoice generation
# invoice_status	ENUM('paid', 'unpaid', 'overdue')	Invoice status
# tax_amount	DECIMAL(10, 2)	Total tax amount applied
# total_invoice_amount	DECIMAL(10, 2)	Final invoice amount
# pdf_path	VARCHAR(255)	Path to the invoice PDF
# created_at	TIMESTAMP	Invoice record creation date
# updated_at	TIMESTAMP	Last update of invoice record



class Invoice(models.Model):
    INVOICE_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('overdue', 'Overdue'),
    ]

    invoice_id = models.AutoField(primary_key=True)
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=20, unique=True)
    invoice_date = models.DateTimeField(auto_now_add=True)
    invoice_status = models.CharField(max_length=10, choices=INVOICE_STATUS_CHOICES, default='unpaid')
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_path = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.get_invoice_status_display}"