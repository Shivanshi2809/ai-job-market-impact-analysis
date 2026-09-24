# AI Impact on Job Market: Benefits vs Risks Analysis

## Problem Statement
Artificial Intelligence is reshaping the global job market at a rapid pace. This
project asks: **does AI adoption create more opportunity (benefit) or more risk
(job displacement) for the modern workforce?** The analysis looks for evidence
in job-level data across industries, company sizes, and salary bands to see
whether automation risk is concentrated among low-paying roles, or spread more
evenly — a question that matters for both workers planning their careers and
organizations planning reskilling programs.

## Dataset
- **Name:** AI-Powered Job Market Insights
- **Source:** Kaggle — https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights
- **Size:** 500 rows, 10 columns
- **Columns:** Job_Title, Industry, Company_Size, Location, AI_Adoption_Level,
  Automation_Risk, Required_Skills, Salary_USD, Remote_Friendly,
  Job_Growth_Projection
- **Note:** This dataset is synthetic (computer-generated) but designed to
  realistically mimic modern job market patterns. Conclusions represent
  patterns within this dataset, not verified real-world employment statistics.

## Methodology
The analysis follows a standard Business Intelligence framework:

1. **Data Cleaning** — checked for missing values and correct data types
2. **Exploratory Data Analysis** — summary statistics, unique value counts
3. **Visualization** — 5 charts covering adoption, risk, salary, growth, and
   company size
4. **Observation → Insight → Hypothesis → Recommendation** — each finding is
   traced from a raw fact in the data to an actionable recommendation, without
   claiming anything the data does not directly support

## Key Findings (Summary)
- ~34% of job roles in the dataset fall under High automation risk
- High-risk roles do **not** show a significant salary penalty — average
  salary for High-risk roles is comparable to (even slightly above) Low-risk
  roles, suggesting automation risk is tied to the *type* of tasks in a role,
  not how well the role pays
- Growth vs Decline projections are spread almost evenly across industries,
  meaning no single industry is uniformly "safe" or "at risk"
- AI adoption level does not vary strongly by company size — small companies
  are adopting AI almost as much as large ones

Full charts and detailed observations/insights/hypotheses/recommendations are
in `ai_job_market_analysis.py` (printed output) and the project report.

## How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Make sure `ai_job_market_insights.csv` is in the same folder as the script
3. Run:
   ```
   python ai_job_market_analysis.py
   ```
4. The script prints the full EDA to the console and saves 5 chart images
   (`chart1_...png` to `chart5_...png`) in the same folder

## Files in this Repository
| File | Description |
|---|---|
| `ai_job_market_analysis.py` | Main analysis code |
| `ai_job_market_insights.csv` | Dataset used |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |
| Project Report (.docx) | Full written report with charts and findings |

## Limitations
- Dataset is synthetic; results reflect statistical patterns within the data,
  not confirmed real-world labor market outcomes
- No time-series data is available in this version, so trends over time
  (e.g. year-by-year AI adoption growth) could not be analyzed
