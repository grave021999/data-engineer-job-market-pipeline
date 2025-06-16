import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw data.
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values with 'Unknown'
    df.fillna("Unknown", inplace=True)

    # Normalize job_skills column
    if 'job_skills' in df.columns:
        df['job_skills'] = df['job_skills'].str.lower()

    # Normalize job_title
    if 'job_title' in df.columns:
        df['job_title'] = df['job_title'].str.title()

    # Normalize job_location
    if 'job_location' in df.columns:
        df['job_location'] = df['job_location'].str.title()

    print("✅ Data transformation complete.")
    return df


def extract_skills(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract individual skills from 'job_skills' column and explode into separate rows.
    """
    if 'job_skills' not in df.columns:
        print("⚠ 'job_skills' column not found.")
        return df

    # Split skills by comma
    df['skills_list'] = df['job_skills'].str.split(',')

    # Explode into individual rows
    df_exploded = df.explode('skills_list')

    # Clean skills: remove spaces and lowercase
    df_exploded['skills_list'] = df_exploded['skills_list'].str.strip().str.lower()

    print("✅ Skill extraction complete.")
    return df_exploded
