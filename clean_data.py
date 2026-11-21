from pathlib import Path
import pandas as pd

# Resolve paths relative to this script's location
BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "HR-Employee-Attrition.csv"
CLEAN_FILE = BASE_DIR / "HR_Employee_Attrition_cleaned.csv"


def clean_hr_data(raw_path: Path, clean_path: Path) -> pd.DataFrame:
  # 1. Load raw dataset
  df = pd.read_csv(raw_path)
  print(f"Raw shape: {df.shape[0]} rows, {df.shape[1]} columns")

  # 2. Standardize column names to snake_case
  df.columns = (
      df.columns.str.strip()
      .str.replace(r"([a-z0-9])([A-Z])", r"\1_\2", regex=True)
      .str.lower()
  )

  # 3. Check missing values and exact duplicates
  missing = df.isna().sum()
  print("\nMissing values:")
  print(missing[missing > 0] if (missing > 0).any() else "No missing values found")
  print("Exact duplicate rows:", df.duplicated().sum())

  # Drop exact duplicate rows if any exist
  if df.duplicated().sum() > 0:
    df = df.drop_duplicates().reset_index(drop=True)

  # 4. Drop single-value (constant) columns and non-analytical ID column
  constant_cols = [col for col in df.columns if df[col].nunique(dropna=False) <= 1]
  cols_to_drop = list(dict.fromkeys(constant_cols + ["employee_number"]))
  existing_drops = [col for col in cols_to_drop if col in df.columns]
  df = df.drop(columns=existing_drops)
  print("\nDropped columns:", existing_drops)

  # 5. Strip whitespace in text columns (avoids Pandas 4 select_dtypes warning)
  text_cols = df.select_dtypes(include=["object", "string"]).columns
  for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

  # Convert empty strings in text columns to missing values if present
  for col in text_cols:
    df[col] = df[col].replace("", pd.NA)

  # 6. Create binary attrition flag (1 = Yes, 0 = No)
  if "attrition" in df.columns:
    df["attrition_flag"] = df["attrition"].map({"Yes": 1, "No": 0})

  # 7. Add readable labels for ordinal 1-4 rating scales
  satisfaction_map = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}
  rating_cols = [
      "environment_satisfaction",
      "job_satisfaction",
      "job_involvement",
      "work_life_balance",
  ]
  for col in rating_cols:
    if col in df.columns:
      df[f"{col}_label"] = df[col].map(satisfaction_map)

  # 8. Save cleaned dataset
  df.to_csv(clean_path, index=False)
  print(f"\nCleaned data saved to: {clean_path.name}")
  print(f"Cleaned shape: {df.shape[0]} rows, {df.shape[1]} columns")

  return df


if __name__ == "__main__":
  cleaned_df = clean_hr_data(RAW_FILE, CLEAN_FILE)