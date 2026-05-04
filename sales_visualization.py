"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 4
Chat Gpt Assistance
"""
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load CSV and convert date column."""
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])

    print("\n--- Loaded Data ---")
    print(df)

    return df


def line_chart(df):
    """Line chart: total sales over time."""
    daily_sales = df.groupby("date")["sales"].sum()

    plt.figure()
    plt.plot(daily_sales.index, daily_sales.values, marker="o")

    plt.title("Total Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def bar_chart(df):
    """Bar chart: sales by product."""
    product_sales = df.groupby("product")["sales"].sum()

    plt.figure()
    plt.bar(product_sales.index, product_sales.values)

    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")

    plt.tight_layout()
    plt.show()


def histogram(df):
    """Histogram: distribution of sales."""
    plt.figure()
    plt.hist(df["sales"], bins=5)

    plt.title("Distribution of Sales Values")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


def main():
    df = pd.read_csv("salesS_data.csv")

    line_chart(df)
    bar_chart(df)
    histogram(df)


if __name__ == "__main__":
    main()