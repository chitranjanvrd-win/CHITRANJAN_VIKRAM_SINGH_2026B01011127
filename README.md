# HR Employee Attrition Data Cleaning & Exploratory Analysis

## Overview
This project cleans and explores the **HR Employee Attrition** dataset (`HR-Employee-Attrition.csv`, 1,470 employee records) using Python (`pandas` and `matplotlib`) in VS Code.

## Project Structure
- `HR-Employee-Attrition.csv` — Raw input dataset
- `clean_data.py` — Data cleaning, column standardization (`snake_case`), constant/ID column removal, text normalization, and feature mapping
- `HR_Employee_Attrition_cleaned.csv` — Cleaned dataset (1,470 rows, 32 columns)
- `eda.py` — Exploratory data analysis across roles, marital status, and numerical metrics
- `charts.py` — Generates visual summary charts
- `charts/` — Output visualizations (`attrition_by_job_role.png`, `avg_income_by_attrition.png`)

## Data Cleaning Steps (`clean_data.py`)
1. Standardized all column headers to `snake_case`.
2. Checked for missing values (`0` missing) and exact duplicate rows (`0` duplicates).
3. Dropped non-informative constant and ID columns (`employee_count`, `over18`, `standard_hours`, `employee_number`).
4. Trimmed whitespace in string columns, added `attrition_flag` (`1` = `Yes`, `0` = `No`), and mapped `1–4` satisfaction/rating scales to readable labels.

## Key Findings (`eda.py` & `charts/`)
- **Role Differences:** Attrition is highest among **Sales Representatives** (`39.76%`), **Laboratory Technicians** (`23.94%`), and **Human Resources** (`23.08%`), while **Managers** (`4.90%`) and **Research Directors** (`2.50%`) have much lower attrition.
- **Compensation Gap:** Employees who left earned an average monthly income of **$4,787.09** compared to **$6,832.74** for employees who stayed.
- **Tenure & Demographics:** Employees who left had shorter average company tenure (`5.13` vs. `7.37` years), shorter time in their current role (`2.90` vs. `4.48` years), lower average age (`33.61` vs. `37.56`), and higher attrition among **Single** employees (`25.53%`).

## How to Run
```bash
python clean_data.py
python eda.py
python charts.py