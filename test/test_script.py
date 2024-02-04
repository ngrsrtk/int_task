import pandas as pd
import pytest
from src.compute import compute_revenue_tasks

# Mock data for testing
@pytest.fixture
def mock_data():
    data = {
        'order_id': [1, 2, 3, 4],
        'customer_id': [101, 102, 101, 103],
        'order_date': ['2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02'],
        'product_id': [1, 2, 1, 3],
        'product_name': ['ProductA', 'ProductB', 'ProductA', 'ProductC'],
        'product_price': [10.0, 20.0, 10.0, 30.0],
        'quantity': [2, 1, 3, 1],
    }
    return pd.DataFrame(data)

def test_monthly_revenue(mock_data):
    result = compute_revenue_tasks(mock_data)
    assert result['monthly_revenue'].tolist() == [60.0, 70.0]

def test_product_revenue(mock_data):
    result = compute_revenue_tasks(mock_data)
    assert result['product_revenue'].tolist() == [20.0, 20.0, 30.0]

def test_customer_revenue(mock_data):
    result = compute_revenue_tasks(mock_data)
    assert result['customer_revenue'].tolist() == [30.0, 20.0, 30.0]

def test_top_customers(mock_data):
    result = compute_revenue_tasks(mock_data)
    assert result['top_customers'].tolist() == [101, 103, 102]
