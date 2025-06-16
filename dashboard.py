import pandas as pd
import streamlit as st

# Load processed data
skills_file = "data/processed/top_skills.csv"

st.set_page_config(page_title="Data Engineering Job Market Dashboard", layout="wide")

st.title("🚀 Data Engineering Job Market — Top Skills Dashboard")
st.write("Analyzed job postings to extract most in-demand skills for data engineers.")

# Load the skills data
try:
    skill_counts = pd.read_csv(skills_file, index_col=0)
    skill_counts = skill_counts.sort_values("count", ascending=False)

    # Sidebar filter
    top_n = st.sidebar.slider("Top N skills to show", min_value=5, max_value=50, value=20, step=5)

    st.subheader(f"Top {top_n} In-Demand Skills")
    st.bar_chart(skill_counts.head(top_n))

    # Show full table
    with st.expander("See Full Skill Frequency Table"):
        st.dataframe(skill_counts)

except Exception as e:
    st.error(f"Error loading data: {e}")
