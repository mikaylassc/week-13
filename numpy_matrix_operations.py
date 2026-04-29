"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 1: NumPy Arrays and Matrix Operations
Chat Gpt Assistance
"""
# numpy_matrix_operations.py

import numpy as np

def create_array():
    """Create a NumPy array with values from 1 to 100."""
    try:
        arr = np.arange(1, 101)
        print("Original Array:\n", arr)
        return arr
    except Exception as e:
        print("Error creating array:", e)
        return None


def reshape_array(arr):
    """Reshape the array into a 10x10 matrix."""
    try:
        matrix = arr.reshape(10, 10)
        print("\n10x10 Matrix:\n", matrix)
        return matrix
    except Exception as e:
        print("Error reshaping array:", e)
        return None


def extract_rows(matrix):
    """Extract rows 5 through 8 (index 4 to 7)."""
    try:
        rows = matrix[4:8]
        print("\nRows 5 to 8:\n", rows)
        return rows
    except Exception as e:
        print("Error extracting rows:", e)
        return None


def compute_sum(matrix):
    """Compute the sum of all elements in the matrix."""
    try:
        total = np.sum(matrix)
        print("\nSum of all elements:", total)
        return total
    except Exception as e:
        print("Error computing sum:", e)
        return None


def main():
    """Main function to run all tasks."""
    arr = create_array()
    
    if arr is not None:
        matrix = reshape_array(arr)
        
        if matrix is not None:
            extract_rows(matrix)
            compute_sum(matrix)


# Run the program
if __name__ == "__main__":
    main()