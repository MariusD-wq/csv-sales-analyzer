from pathlib import Path

import pandas as pd


def load_sales(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)


def add_revenue_column(sales: pd.DataFrame) -> pd.DataFrame:
    result = sales.copy()

    result["revenue"] = result["quantity"] * result["price"]

    return result


def calculate_total_revenue(sales: pd.DataFrame) -> float:
    return float(sales["revenue"].sum())
