from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CLEAN_FILE = BASE_DIR / "HR_Employee_Attrition_cleaned.csv"

df = pd.read_csv(CLEAN_FILE)
print(f"Loaded cleaned data: {df.shape[0]} rows, {df.shape[1]} columns\n")

# 1. Overall attrition rate
if "attrition_flag" in df.columns:
  overall_rate = df["attrition_flag"].mean() * 100
  counts = df["attrition"].value_counts() if "attrition" in df.columns else None
  print(f"Overall Attrition Rate: {overall_rate:.2f}%")
  if counts is not None:
    print(counts.to_string(), "\n")

# 2. Attrition rate by key categorical factors
group_cols = [
    c
    for c in [
        "over_time",
        "department",
        "job_role",
        "marital_status",
        "job_satisfaction_label",
        "work_life_balance_label",
    ]
    if c in df.columns
]

for col in group_cols:
  summary = (
      df.groupby(col, dropna=False)["attrition_flag"]
      .agg(employees="count", attrition_rate=lambda s: round(s.mean() * 100, 2))
      .sort_values("attrition_rate", ascending=False)
  )
  print(f"--- Attrition by {col} ---")
  print(summary.to_string(), "\n")

# 3. Numeric comparison: stayed vs. left
num_cols = [
    c
    for c in [
        "age",
        "monthly_income",
        "distance_from_home",
        "years_at_company",
        "years_in_current_role",
    ]
    if c in df.columns
]
if num_cols and "attrition" in df.columns:
  print("--- Average Metrics by Attrition ---")
  print(df.groupby("attrition")[num_cols].mean().round(2).to_string())