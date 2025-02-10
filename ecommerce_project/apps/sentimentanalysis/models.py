from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order
from products.models import Products
import uuid

# Proposed Table Schema
# Column Name	Data Type	Description
# id	UUID (Primary Key)	Unique identifier for the sentiment record
# customer_id	ForeignKey	Reference to the customer table
# order_id	ForeignKey	Reference to the order table (optional)
# feedback_text	Text	Raw feedback provided by the customer
# sentiment_score	Decimal (5, 2)	Sentiment score ranging from -1.00 to 1.00
# sentiment_label	Char (20)	Label for sentiment (Positive, Neutral, Negative)
# created_at	DateTime	Timestamp when the feedback was submitted
# processed_at	DateTime	Timestamp when sentiment analysis was completed
# product_id	ForeignKey	Reference to the product table
# executive_action	Boolean	Whether customer care took action on feedback




class SentimentAnalysis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, limit_choices_to={"role":"User"})
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    feedback_text = models.TextField()
    sentiment_score = models.DecimalField(max_digits=5,decimal_places=2)
    sentiment_label = models.CharField(max_length=20, choices=[
        ('Positive', 'Positive'),
        ('Neutral', 'Neutral'),
        ('Negative', 'Negative')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    executive_action = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Sentiment Analysis"
        verbose_name_plural = "Sentiment Analyses"
    
    def __str__(self):
        return f"{self.customer} - {self.sentiment_label}"
