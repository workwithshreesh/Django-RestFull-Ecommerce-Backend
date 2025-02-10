from django.db import models
from django.contrib.auth import get_user_model


# Customer Ticket Table (Support Ticket System)
# Column Name	Data Type	Description
# ticket_id	INT (PK)	Unique Ticket ID
# customer_id	INT (FK)	Reference to the customer
# issue_type	ENUM('billing', 'order', 'technical', 'other')	Type of issue
# description	TEXT	Detailed issue description
# ticket_status	ENUM('open', 'in_progress', 'resolved', 'closed')	Ticket status
# created_at	TIMESTAMP	Ticket creation timestamp
# updated_at	TIMESTAMP	Last ticket update timestamp
# assigned_agent_id	INT (FK)	Assigned customer care agent




# Agent Table
# Column Name	Data Type	Description
# agent_id	INT (PK)	Unique Agent ID
# name	VARCHAR(100)	Agent's Full Name
# email	VARCHAR(100)	Agent's Email Address
# phone_number	VARCHAR(20)	Contact Number
# role	ENUM('junior', 'senior', 'team_lead')	Agent's role in the support team
# availability_status	ENUM('available', 'busy', 'offline')	Agent's current status
# assigned_tickets	INT	Count of assigned tickets
# created_at	TIMESTAMP	Record creation timestamp
# updated_at	TIMESTAMP	Last record update timestamp



class CustomerTickets(models.Model):
    Ticket_Id = models.AutoField(primary_key=True,null=False)
    User_Id = models.ForeignKey(get_user_model(),null=False, on_delete=models.CASCADE)
    Issue_Type = models.CharField(max_length=30, choices=[
        ("Billing","Billing"),
        ("Order","Order"),
        ("Technical","Technical"),
        ("Other","Other")
    ])
    Description = models.TextField()
    Ticket_Status = models.CharField(max_length=30, choices=[
        ("Open","Open"),
        ("In Progress","In Progress"),
        ("Resolved","Resolved"),
        ("Closed","Closed")
    ])
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now_add=True)
    # Assigned_Agent_Id = models.ForeignKey()
