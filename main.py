from pathlib import Path

from sales import (
    add_revenue_column,
    calculate_total_revenue,
    load_sales,
)


def main():
    sales = load_sales(Path("sales.csv"))
    sales = add_revenue_column(sales)

    print(sales)

    total = calculate_total_revenue(sales)

    print()
    print(f"Total Revenue: {total:.2f}")


if __name__ == "__main__":
    main()
