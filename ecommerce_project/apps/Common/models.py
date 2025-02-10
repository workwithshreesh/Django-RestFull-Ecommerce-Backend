from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model

# Coupons
# Column Name	Data Type	Description
# id	Primary Key	Unique coupon ID
# code	String	Coupon code
# discount_percent	Decimal	Discount percentage
# valid_till	Date	Expiration date
# is_active	Boolean	Active status

class Coupons(models.Model):
    Coupon_Id = models.AutoField(primary_key=True, null=False)
    Coupon_Code = models.CharField(max_length=50)
    Discount_Percent = models.DecimalField(max_digits=10, decimal_places=2)
    Valid_Till = models.DateField()
    Is_Active = models.BooleanField()


# Review
# Column Name	Data Type	Description
# id	Primary Key	Unique review ID
# product_id	Foreign Key	Reference to Products
# user_id	Foreign Key	Reference to Users
# rating	Integer	Rating out of 5
# review_text	Text	User review text
# created_at	DateTime	Review creation time



class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE) 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)       
    rating = models.IntegerField(choices=[(1, '1 Star'), 
                                          (2, '2 Stars'), 
                                          (3, '3 Stars'), 
                                          (4, '4 Stars'), (5, '5 Stars')])  
    review_text = models.TextField()  # Review text
    created_at = models.DateTimeField(auto_now_add=True)  





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



class Loyalty(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    points_earned = models.IntegerField(default=0)
    points_spent = models.IntegerField(default=0)
    loyalty_status = models.CharField(max_length=20, default='Active')
    membership_level = models.CharField(max_length=20, default='Bronze')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Loyalty status for {self.user.username}"

    class Meta:
        db_table = 'loyalty'  
