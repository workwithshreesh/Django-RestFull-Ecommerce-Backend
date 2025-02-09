from django.db import models

# Column Name	Data Type	Description
# id	Primary Key	Unique request ID
# customer_id	Foreign Key	Reference to Users
# request_type	Enum	Cancel/Query/Support
# status	Enum	Open/Resolved/Pending
# created_at	DateTime	Request creation time
# resolved_at	DateTime	Resolution time (if resolved)




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



# Customer Return Request Table
# Column Name	Data Type	Description
# return_request_id	INT (PK)	Unique Return Request ID
# customer_id	INT (FK)	Reference to the customer
# order_item_id	INT (FK)	Reference to the specific order item
# product_id	INT (FK)	Reference to the product being returned
# return_reason	TEXT	Customer's reason for the return
# return_status	ENUM('requested', 'approved', 'rejected', 'completed')	Return request status
# requested_at	TIMESTAMP	Return request date
# updated_at	TIMESTAMP	Last update timestamp
