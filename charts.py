from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CLEAN_FILE = BASE_DIR / "HR_Employee_Attrition_cleaned.csv"
CHARTS_DIR = BASE_DIR / "charts"
CHARTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(CLEAN_FILE)

# 1. Attrition Rate (%) by Job Role
if {"job_role", "attrition_flag"}.issubset(df.columns):
  role_rate = (
      df.groupby("job_role")["attrition_flag"]
      .mean()
      .mul(100)
      .sort_values(ascending=True)
  )

  fig, ax = plt.subplots(figsize=(9, 5))
  role_rate.plot(kind="barh", ax=ax, color="#2b6cb0")
  ax.set_title("Attrition Rate by Job Role", fontsize=13, fontweight="bold")
  ax.set_xlabel("Attrition Rate (%)")
  ax.set_ylabel("")
  ax.bar_label(ax.containers[0], fmt="%.1f%%", padding=3, fontsize=9)
  ax.set_xlim(0, role_rate.max() * 1.15)
  plt.tight_layout()
  plt.savefig(CHARTS_DIR / "attrition_by_job_role.png", dpi=150)
  plt.close()

# 2. Average Monthly Income by Attrition Status
if {"attrition", "monthly_income"}.issubset(df.columns):
  avg_income = df.groupby("attrition")["monthly_income"].mean()

  fig, ax = plt.subplots(figsize=(6, 4.5))
  avg_income.plot(kind="bar", ax=ax, color=["#2f855a", "#c53030"])
  ax.set_title(
      "Average Monthly Income by Attrition", fontsize=13, fontweight="bold"
  )
  ax.set_xlabel("Attrition")
  ax.set_ylabel("Average Monthly Income ($)")
  ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
  ax.bar_label(ax.containers[0], fmt="$%.0f", padding=3, fontsize=10)
  ax.set_ylim(0, avg_income.max() * 1.15)
  plt.tight_layout()
  plt.savefig(CHARTS_DIR / "avg_income_by_attrition.png", dpi=150)
  plt.close()

print(f"Charts saved in: {CHARTS_DIR}")