"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3
Chat Gpt Assistance
"""
import pandas as pd


def load_data(file_path):
    """Load dataset and display first 5 rows."""
    df = pd.read_csv(file_path)
    print("\n--- First 5 Rows ---")
    print(df.head())
    return df


def check_missing(df):
    """Check for missing values."""
    print("\n--- Missing Values Per Column ---")
    print(df.isna().sum())


def fill_missing(df):
    """Fill missing values using median and mean rules."""
    df["units_sold"] = df["units_sold"].fillna(df["units_sold"].median())
    df["unit_price"] = df["unit_price"].fillna(df["unit_price"].mean())

    print("\n--- After Filling Missing Values ---")
    print(df)
    return df


def remove_duplicates(df):
    """Remove duplicate rows and show counts."""
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print("\n--- Duplicate Removal ---")
    print(f"Rows before: {before}")
    print(f"Rows after: {after}")

    return df


def encode_categorical(df):
    """One-hot encode categorical columns."""
    df_encoded = pd.get_dummies(df, columns=["region", "product"])

    print("\n--- After One-Hot Encoding (Columns) ---")
    print(df_encoded.columns)

    return df_encoded


def normalize_columns(df):
    """Min-max normalize numeric columns."""
    for col in ["units_sold", "unit_price"]:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)

    print("\n--- After Normalization ---")
    print(df)

    return df


def group_summary(df_original):
    """Group by region and calculate summary stats."""
    summary = df_original.groupby("region").agg(
        total_units_sold=("units_sold", "sum"),
        avg_unit_price=("unit_price", "mean")
    )

    print("\n--- Grouped Summary by Region ---")
    print(summary)


def main():
    """Main execution pipeline."""

    # Task 1: Load data
    df = load_data("sales_data.csv")

    # Task 2: Missing values
    check_missing(df)

    # Task 3: Fill missing values
    df = fill_missing(df)

    # Task 4: Remove duplicates
    df_clean = remove_duplicates(df)

    # Task 7 (must use original cleaned BEFORE encoding)
    group_summary(df_clean)

    # Task 5: One-hot encoding
    df_encoded = encode_categorical(df_clean)

    # Task 6: Normalization
    df_final = normalize_columns(df_encoded)


if __name__ == "__main__":
    main()