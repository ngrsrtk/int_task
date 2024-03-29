import pandas as pd
from datetime import datetime

def compute_revenue_tasks(data):
    # Task 1: Compute total revenue generated by the online store for each month
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['month'] = data['order_date'].dt.month
    monthly_revenue = data.groupby('month')['product_price'].sum()

    # Task 2: Compute total revenue generated by each product
    product_revenue = data.groupby('product_id')['product_price'].sum()

    # Task 3: Compute total revenue generated by each customer
    customer_revenue = data.groupby('customer_id')['product_price'].sum()

    # Task 4: Identify the top 10 customers by revenue
    top_customers = customer_revenue.nlargest(10)

    return {
        'monthly_revenue': monthly_revenue,
        'product_revenue': product_revenue,
        'customer_revenue': customer_revenue,
        'top_customers': top_customers,
    }
