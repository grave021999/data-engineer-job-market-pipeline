import pandas as pd

def load_data(df: pd.DataFrame, output_path: str):
    """
    Load cleaned data to processed folder as CSV.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"✅ Successfully saved processed data to {output_path}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
