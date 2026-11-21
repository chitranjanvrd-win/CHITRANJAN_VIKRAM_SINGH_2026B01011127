# Software Requirements Specification (SRS)
## HR Employee Attrition Data Analysis Project

- **Prepared by:** Chitranjan Vikram Singh (`2026B01011127`, B.Tech CSE — Section 5)
- **GitHub Repository:** `https://github.com/chitranjanvrd-win/CHITRANJAN_VIKRAM_SINGH_2026B01011127`
- **Folder:** `hr_attrition_analysis`
- **Tools Used:** Visual Studio Code, Python 3.15 (64-bit), Windows PowerShell, Git

---

## 1. What This Project Is About
This project takes the raw IBM HR Employee Attrition dataset (`HR-Employee-Attrition.csv`, **1,470** rows) and turns it into a clean dataset, a set of summary findings, visual charts, and clear project documentation[cite: 6, 15]. The goal was to build a straightforward, repeatable workflow in Python where each script handles one clear stage of the analysis.

---

## 2. What I Built

### Data Cleaning (`clean_data.py`)
- Reads `HR-Employee-Attrition.csv` (**1,470** employee records) using `pandas` and `pathlib`[cite: 6, 7].
- Renames columns to clean `snake_case`, trims extra spaces in text columns, and checks for missing values and duplicate rows.
- Removes columns that do not add analytical value (`employee_count`, `over18`, `standard_hours`, `employee_number`).
- Adds `attrition_flag` (`1` for `Yes`, `0` for `No`) and readable labels for rating scales, then saves the result to `HR_Employee_Attrition_cleaned.csv` (**1,470 rows, 32 columns**)[cite: 6].

### Exploratory Data Analysis (`eda.py`)
- Loads `HR_Employee_Attrition_cleaned.csv` and checks the overall attrition rate alongside breakdowns across `over_time`, `department`, `job_role`, `marital_status`, `job_satisfaction_label`, and `work_life_balance_label`[cite: 7].
- Compares averages for `age`, `monthly_income`, `distance_from_home`, `years_at_company`, and `years_in_current_role` between employees who stayed (`No`) and those who left (`Yes`)[cite: 7, 8].
- Highlights the clearest patterns in the data: **Sales Representatives** (**39.76%**), **Laboratory Technicians** (**23.94%**), **Human Resources** (**23.08%**), and **Single** employees (**25.53%**) have higher attrition, and employees who left earned a lower average monthly income (**$4,787.09**) than those who stayed (**$6,832.74**)[cite: 8].

### Charts (`charts.py` & `charts/`)
- Uses `matplotlib` (`3.11.2`) to create the `charts/` folder automatically and export two PNG visuals[cite: 10, 11]:
  - `charts/attrition_by_job_role.png` — shows attrition rates across job roles.
  - `charts/avg_income_by_attrition.png` — compares average monthly income between employees who stayed and left[cite: 8, 11].

### Documentation (`README.md` & `srs.md`)
- `README.md` gives a quick overview of the files, cleaning steps, key findings, and run commands[cite: 15].
- `srs.md` lays out the project's purpose, components, and step-by-step build process.

---

## 3. How I Built It

1. **Set up the folder and scripts in VS Code:** Created `hr_attrition_analysis`, added `HR-Employee-Attrition.csv`, and worked in the integrated PowerShell terminal[cite: 6, 10].
2. **Cleaned the dataset first:** Wrote `clean_data.py` and ran `python clean_data.py` to generate `HR_Employee_Attrition_cleaned.csv` (**1,470 rows, 32 columns**)[cite: 6].
3. **Explored the numbers:** Wrote `eda.py` and ran `python eda.py` to inspect attrition across roles, marital status, pay, and tenure[cite: 7, 8].
4. **Generated the charts:** Installed `matplotlib`, wrote `charts.py`, and ran `python charts.py` to save the two charts inside `charts/`[cite: 9, 10, 11].
5. **Wrote docs and pushed to GitHub:** Added `README.md` at the project root, initialized Git (`git init`), committed the files, connected `origin` to `https://github.com/chitranjanvrd-win/CHITRANJAN_VIKRAM_SINGH_2026B01011127.git`, sorted out the `README.md` merge conflict, and pushed everything to `main`[cite: 13, 15].