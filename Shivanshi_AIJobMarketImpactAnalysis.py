"""
AI Impact on Job Market: Benefits vs Risks Analysis
-----------------------------------------------------
Dataset: AI-Powered Job Market Insights (Kaggle)
Source: https://www.kaggle.com/datasets/uom190346a/ai-powered-job-market-insights

This script performs a complete Exploratory Data Analysis (EDA) to answer:
"Does AI adoption create more opportunity (benefit) or more risk (job loss)
in the modern job market?"

Framework followed: Observation -> Insight -> Hypothesis -> Recommendation
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)

# -----------------------------------------------------------------
# STEP 1: LOAD DATA
# -----------------------------------------------------------------
df = pd.read_csv("ai_job_market_insights.csv")

print("=" * 70)
print("STEP 1: BASIC DATA OVERVIEW")
print("=" * 70)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nColumn names and data types:")
print(df.dtypes)
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------------------------------------
# STEP 2: SUMMARY STATISTICS
# -----------------------------------------------------------------
print("\n" + "=" * 70)
print("STEP 2: SUMMARY STATISTICS")
print("=" * 70)
print(df["Salary_USD"].describe())

print("\nUnique values in key categorical columns:")
for col in ["Industry", "AI_Adoption_Level", "Automation_Risk",
            "Job_Growth_Projection", "Company_Size"]:
    print(f"\n{col}:")
    print(df[col].value_counts())

# -----------------------------------------------------------------
# STEP 3: VISUALIZATIONS (5 charts)
# -----------------------------------------------------------------

# Chart 1: AI Adoption Level by Industry
plt.figure()
adoption_industry = pd.crosstab(df["Industry"], df["AI_Adoption_Level"])
adoption_industry.plot(kind="bar", stacked=True, colormap="viridis",
                        ax=plt.gca())
plt.title("Chart 1: AI Adoption Level by Industry")
plt.xlabel("Industry")
plt.ylabel("Number of Job Roles")
plt.xticks(rotation=45, ha="right")
plt.legend(title="AI Adoption Level")
plt.tight_layout()
plt.savefig("chart1_ai_adoption_by_industry.png", dpi=150)
plt.close()

# Chart 2: Automation Risk Distribution (Pie Chart)
plt.figure()
risk_counts = df["Automation_Risk"].value_counts()
colors = ["#e74c3c", "#f39c12", "#2ecc71"]
plt.pie(risk_counts, labels=risk_counts.index, autopct="%1.1f%%",
        colors=colors, startangle=90)
plt.title("Chart 2: Automation Risk Distribution")
plt.tight_layout()
plt.savefig("chart2_automation_risk_distribution.png", dpi=150)
plt.close()

# Chart 3: Salary by Automation Risk (Box Plot)
plt.figure()
sns.boxplot(data=df, x="Automation_Risk", y="Salary_USD",
            order=["Low", "Medium", "High"], hue="Automation_Risk",
            palette="Set2", legend=False)
plt.title("Chart 3: Salary Distribution by Automation Risk Level")
plt.xlabel("Automation Risk")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.savefig("chart3_salary_by_automation_risk.png", dpi=150)
plt.close()

# Chart 4: Job Growth Projection by Industry
plt.figure()
growth_industry = pd.crosstab(df["Industry"], df["Job_Growth_Projection"])
growth_industry.plot(kind="bar", stacked=True, colormap="coolwarm",
                      ax=plt.gca())
plt.title("Chart 4: Job Growth Projection by Industry")
plt.xlabel("Industry")
plt.ylabel("Number of Job Roles")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Growth Projection")
plt.tight_layout()
plt.savefig("chart4_job_growth_by_industry.png", dpi=150)
plt.close()

# Chart 5: Company Size vs AI Adoption Level
plt.figure()
size_adoption = pd.crosstab(df["Company_Size"], df["AI_Adoption_Level"])
size_adoption.plot(kind="bar", colormap="plasma", ax=plt.gca())
plt.title("Chart 5: Company Size vs AI Adoption Level")
plt.xlabel("Company Size")
plt.ylabel("Number of Job Roles")
plt.xticks(rotation=0)
plt.legend(title="AI Adoption Level")
plt.tight_layout()
plt.savefig("chart5_company_size_vs_adoption.png", dpi=150)
plt.close()

print("\nAll 5 charts saved successfully.")

# -----------------------------------------------------------------
# STEP 4: KEY CALCULATIONS FOR OBSERVATIONS / INSIGHTS
# -----------------------------------------------------------------
avg_salary_by_risk = df.groupby("Automation_Risk")["Salary_USD"].mean().round(2)
avg_salary_by_adoption = df.groupby("AI_Adoption_Level")["Salary_USD"].mean().round(2)
top_industry_high_risk = (
    df[df["Automation_Risk"] == "High"]["Industry"].value_counts().idxmax()
)
top_growth_industry = (
    df[df["Job_Growth_Projection"] == "Growth"]["Industry"].value_counts().idxmax()
)
decline_pct = round((df["Job_Growth_Projection"] == "Decline").mean() * 100, 1)
growth_pct = round((df["Job_Growth_Projection"] == "Growth").mean() * 100, 1)
high_risk_pct = round((df["Automation_Risk"] == "High").mean() * 100, 1)

print("\n" + "=" * 70)
print("STEP 4: KEY NUMBERS USED IN OBSERVATIONS")
print("=" * 70)
print(f"Average salary by automation risk:\n{avg_salary_by_risk}\n")
print(f"Average salary by AI adoption level:\n{avg_salary_by_adoption}\n")
print(f"Industry with most High-risk roles: {top_industry_high_risk}")
print(f"Industry with most Growth-projected roles: {top_growth_industry}")
print(f"% roles projected to Decline: {decline_pct}%")
print(f"% roles projected to Grow: {growth_pct}%")
print(f"% roles at High automation risk: {high_risk_pct}%")

# -----------------------------------------------------------------
# STEP 5: OBSERVATIONS, INSIGHTS, HYPOTHESES, RECOMMENDATIONS
# -----------------------------------------------------------------
print("\n" + "=" * 70)
print("STEP 5: OBSERVATIONS -> INSIGHTS -> HYPOTHESES -> RECOMMENDATIONS")
print("=" * 70)

observations = [
    f"1. {high_risk_pct}% of job roles in the dataset fall under High automation risk.",
    f"2. Average salary for High-risk roles is ${avg_salary_by_risk.get('High', 0):,.2f}, "
    f"compared to ${avg_salary_by_risk.get('Low', 0):,.2f} for Low-risk roles.",
    f"3. The industry with the highest count of High-risk roles is {top_industry_high_risk}.",
    f"4. {growth_pct}% of roles are projected to Grow, while {decline_pct}% are projected to Decline.",
    f"5. {top_growth_industry} industry has the highest number of roles projected for Growth.",
]

insights = [
    "1. Automation risk does not show a large salary penalty in this dataset - "
    "high-risk roles are not necessarily low-paying, suggesting risk here is tied "
    "to task type, not skill level.",
    "2. Growth and Decline projections are spread fairly evenly across industries, "
    "indicating AI's impact is uneven even within the same sector - not every role "
    "in a 'growing' industry is safe.",
    "3. Company size does not strongly determine AI adoption level, suggesting AI "
    "tools have become accessible even to smaller companies, not just large enterprises.",
]

hypotheses = [
    "1. If automation risk does not correlate strongly with salary, then simply "
    "earning more may not protect a role from AI-driven disruption - the nature "
    "of tasks matters more than pay grade.",
    "2. If growth/decline is spread unevenly within industries rather than by "
    "industry as a whole, then employees should evaluate their specific role's "
    "task composition, not just their industry's overall AI narrative.",
]

recommendations = [
    "1. Reskilling programs should be targeted at specific high-automation-risk "
    "roles across ALL industries and salary bands, not limited to low-paying jobs.",
    "2. Professionals should track role-level AI exposure (their own tasks) rather "
    "than relying on broad industry-level 'AI is good/bad for my sector' narratives.",
    "3. Organizations should pair AI adoption with structured upskilling paths for "
    "roles flagged at High automation risk, regardless of company size.",
]

for label, items in [("OBSERVATIONS", observations), ("INSIGHTS", insights),
                      ("HYPOTHESES", hypotheses), ("RECOMMENDATIONS", recommendations)]:
    print(f"\n--- {label} ---")
    for item in items:
        print(item)

print("\nAnalysis complete. 5 chart images saved in the current folder.")
