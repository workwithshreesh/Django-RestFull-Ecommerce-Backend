from django.db import models

# Coupons
# Column Name	Data Type	Description
# id	Primary Key	Unique coupon ID
# code	String	Coupon code
# discount_percent	Decimal	Discount percentage
# valid_till	Date	Expiration date
# is_active	Boolean	Active status


# Review
# Column Name	Data Type	Description
# id	Primary Key	Unique review ID
# product_id	Foreign Key	Reference to Products
# user_id	Foreign Key	Reference to Users
# rating	Integer	Rating out of 5
# review_text	Text	User review text
# created_at	DateTime	Review creation time


# CREATE TABLE loyalty (
#   loyalty_id SERIAL PRIMARY KEY,
#   user_id INT NOT NULL,
#   points_earned INT DEFAULT 0,
#   points_spent INT DEFAULT 0,
#   loyalty_status VARCHAR(20) DEFAULT 'Active',
#   membership_level VARCHAR(20) DEFAULT 'Bronze',
#   created_at TIMESTAMP DEFAULT NOW(),
#   updated_at TIMESTAMP DEFAULT NOW(),
#   FOREIGN KEY (user_id) REFERENCES users(user_id)
# );
