from django.db import models

# Column Name	Data Type	Description
# id	Primary Key	Unique inventory ID
# product_id	Foreign Key	Reference to Products
# stock_quantity	Integer	Available stock quantity
# restock_date	Date	Last restock date