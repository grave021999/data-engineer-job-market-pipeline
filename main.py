from etl.extract import extract_data
from etl.transform import transform_data, extract_skills
from etl.load import load_data

def main():
    # File paths
    raw_file_path = "data/raw/postings.csv"
    processed_file_path = "data/processed/clean_postings.csv"
    skills_file_path = "data/processed/skills_postings.csv"

    # Extract raw data
    df_raw = extract_data(raw_file_path)
    
    if df_raw is not None:
        # Transform data (cleaning, normalization)
        df_clean = transform_data(df_raw)
        load_data(df_clean, processed_file_path)

        # Extract individual skills (explode)
        df_skills = extract_skills(df_clean)
        load_data(df_skills, skills_file_path)

if __name__ == "__main__":
    main()
