"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 2: Data Cleaning and Analysis with Pandas Completion requirements
Chat Gpt Assistance
"""
import pandas as pd

def load_data():
    """Load the CSV file and display first 5 rows."""
    try:
        df = pd.read_csv("./employees.csv")
        print("First 5 rows:\n", df.head())
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None


def check_missing_values(df):
    """Display missing values per column."""
    try:
        print("\nMissing values per column:\n", df.isna().sum())
    except Exception as e:
        print("Error checking missing values:", e)


def handle_missing_values(df):
    """
    Handle missing values.
    Option A: Fill missing salary values with average salary.
    """
    try:
        avg_salary = df["salary"].mean()
        df["salary"].fillna(avg_salary, inplace=True)
        
        print("\nDataset after handling missing values:\n", df)
        return df
    except Exception as e:
        print("Error handling missing values:", e)
        return df


def filter_data(df):
    """Filter IT employees with salary > 65000."""
    try:
        filtered = df[(df["department"] == "IT") & (df["salary"] > 65000)]
        print("\nFiltered Data (IT + salary > 65000):\n", filtered)
        return filtered
    except Exception as e:
        print("Error filtering data:", e)
        return None


def sort_data(filtered_df):
    """Sort filtered data by salary descending."""
    try:
        sorted_df = filtered_df.sort_values(by="salary", ascending=False)
        print("\nSorted Data (by salary descending):\n", sorted_df)
        return sorted_df
    except Exception as e:
        print("Error sorting data:", e)
        return filtered_df


def calculate_average(df):
    """Calculate average salary."""
    try:
        avg_salary = df["salary"].mean()
        print("\nAverage salary:", avg_salary)
    except Exception as e:
        print("Error calculating average:", e)


def main():
    """Main function to run all tasks."""
    df = load_data()
    
    if df is not None:
        check_missing_values(df)
        df = handle_missing_values(df)
        filtered = filter_data(df)
        
        if filtered is not None:
            sort_data(filtered)
        
        calculate_average(df)


# Run the program
if __name__ == "__main__":
    main()