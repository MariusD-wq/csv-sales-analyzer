import pandas as pd
from sales import (
    add_revenue_column,
    calculate_total_revenue,
)


def test_add_revenue_column():
    sales = pd.DataFrame(
        {
            "product": ["Laptop", "Mouse"],
            "quantity": [2, 10],
            "price": [1000, 25],
        }
    )

    result = add_revenue_column(sales)

    assert result["revenue"].tolist() == [2000, 250]


def test_calculate_total_revenue():
    sales = pd.DataFrame(
        {
            "product": ["Laptop", "Mouse"],
            "quantity": [2, 10],
            "price": [1000, 25],
            "revenue": [2000, 250],
        }
    )

    assert calculate_total_revenue(sales) == 2250
