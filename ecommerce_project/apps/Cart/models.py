from django.db import models

# Cart Table
# Column Name	Data Type	Description
# id	Primary Key	Unique cart ID
# user_id	Foreign Key	Reference to Users
# created_at	DateTime	Cart creation time
# is_active	Boolean	Indicates if the cart is active


# CartItem
# Column Name	Data Type	Description
# id	Primary Key	Unique cart item ID
# cart_id	Foreign Key	Reference to Cart
# product_id	Foreign Key	Reference to Products
# quantity	Integer	Number of units added
# price	Decimal	Price at the time of addition
# added_at	DateTime	Timestamp for adding product


