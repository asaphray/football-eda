# scripts/data_loader.py

import pandas as pd
import os

def load_fifa_data(folder_path, file_name="fifa data.csv"):
    """
    Load FIFA dataset from a CSV file.

    Args:
        folder_path (str): Path to the folder containing the dataset.
        file_name (str): Name of the dataset file (default is "fifa data.csv").

    Returns:
        pd.DataFrame: Loaded FIFA dataset.
    """
    file_path = os.path.join(folder_path, file_name)  # Dynamically constructing the file path
    return pd.read_csv(file_path)

def basic_cleaning(df):
    """
    Perform basic cleaning on the dataset.

    - Removes duplicate rows.
    - Drops rows with missing values in the 'Overall' column.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = df.drop_duplicates()
    df = df.dropna(subset=["Overall"])
    return df
