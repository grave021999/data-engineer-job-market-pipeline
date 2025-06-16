import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract raw data from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Successfully loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None
