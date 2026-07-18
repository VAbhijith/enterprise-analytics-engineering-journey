import pandas as pd

def load_customers(file_path):
    """
    Load customer data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing customer data.

    Returns:
    pd.DataFrame: A DataFrame containing the customer data.
    """
    try:
        customer_data = pd.read_csv(file_path)
        print("="*60)
        print("Customer data loaded successfully.")
        print("="*60)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    return customer_data