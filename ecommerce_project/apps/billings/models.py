from django.db import models

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
