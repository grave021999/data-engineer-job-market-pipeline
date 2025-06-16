import pandas as pd

def analyze_skills(file_path: str, top_n: int = 20):
    """
    Analyze and print top N most common skills.
    """
    try:
        df = pd.read_csv(file_path)

        # Check if skills_list column exists
        if 'skills_list' not in df.columns:
            print("⚠ 'skills_list' column not found.")
            return

        # Count skill frequencies
        skill_counts = df['skills_list'].value_counts().head(top_n)

        print(f"\n🎯 Top {top_n} most in-demand skills:\n")
        print(skill_counts)

        # Save to CSV
        skill_counts.to_csv("data/processed/top_skills.csv", header=["count"])
        print("\n✅ Top skills saved to data/processed/top_skills.csv")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    analyze_skills("data/processed/skills_postings.csv", top_n=20)
