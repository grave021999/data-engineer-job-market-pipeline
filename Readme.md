<img width="1280" height="579" alt="banner" src="https://github.com/user-attachments/assets/1040410c-8017-489e-ad87-e0a80e5fb51b" />
# 🚀 Data Engineering Job Market Pipeline

**Data Engineering Job Market Pipeline** is an end-to-end mini project designed to analyze job postings and identify the most in-demand skills for Data Engineers. It demonstrates a practical ETL workflow, skill extraction logic, data processing, and dashboard-based visualization.

---

## 🔧 Project Overview

In this project, we:

- Built a fully functional **ETL pipeline** using Python  
- Extracted and cleaned raw job posting data  
- Normalized and exploded job skills into individual records  
- Aggregated the most frequently demanded skills  
- Built a live interactive dashboard using Streamlit  
- Deployed the project to Streamlit Cloud  

---

## 🗂️ Project Structure

```text
data_engineer_job_pipeline/
│
├── data/
│   ├── raw/                 # Raw input data
│   └── processed/           # Cleaned & processed data
│
├── etl/
│   ├── extract.py           # Extraction logic
│   ├── transform.py         # Transformation & skill extraction
│   └── load.py              # Load logic
│
├── dq/                      # Data quality (future extension)
├── orchestration/           # Orchestration (future extension)
│
├── main.py                  # ETL pipeline runner
├── skills_analysis.py       # Skill aggregation & analysis
├── dashboard.py             # Streamlit dashboard
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## 📊 Sample Output

- ✅ Top skills extracted: **Python, SQL, Azure, AWS, Spark, Data Pipelines, ETL**, and more  
- ✅ Clean processed dataset: `data/processed/skills_postings.csv`  
- ✅ Aggregated skill counts: `data/processed/top_skills.csv`  
- ✅ Live dashboard visualizing the most in-demand skills  

---

## 💻 Tech Stack

| Category            | Tools / Technologies                |
|--------------------|-------------------------------------|
| Programming        | Python                              |
| Data Processing    | Pandas                              |
| Dashboard          | Streamlit                           |
| Orchestration      | Prefect *(upcoming)*                |
| Data Quality       | Great Expectations *(upcoming)*     |

---

## 🚀 Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/data-engineer-job-market-pipeline.git
cd data-engineer-job-market-pipeline
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.\.venv\Scripts\Activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the ETL Pipeline
```bash
python main.py
```

### 5️⃣ Run Skills Analysis
```bash
python skills_analysis.py
```

### 6️⃣ Run the Streamlit Dashboard
```bash
streamlit run dashboard.py
```

---

## 🔥 Future Enhancements

- Add **data quality validation** with Great Expectations  
- Add **Prefect orchestration** for production-grade pipelines  
- Extend deployment to **Azure, AWS, or GCP**  
- Build a **Resume Matcher** to compare resume skills with job market demand  

---

## 📣 Author

**Mohammad Atif**  
**Data Engineer | Open to Work 🔎**

- LinkedIn: https://www.linkedin.com/in/atif0201/

---

## ⭐ Project Status

**WORKING ✅**
