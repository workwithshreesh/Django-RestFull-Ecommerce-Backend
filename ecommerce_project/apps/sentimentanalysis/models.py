from django.db import models

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
