import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "datasets", "qs_data_cleaned.csv")

df = pd.read_csv(FILE_PATH)

df["qs_overall_score"] = pd.to_numeric(df["qs_overall_score"], errors="coerce")
df = df.dropna(subset=["qs_overall_score"])

PLOTS_DIR = os.path.join(BASE_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

print(df.head())
print(df.describe())
print(df.columns)

numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=False, cmap="coolwarm")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "correlation_heatmap.png"))
plt.close()

top20 = df.nlargest(20, "qs_overall_score")
print(top20[["institution_name", "qs_overall_score", "2025_rank"]])

scatter_pairs = [
    ("academic_reputation", "qs_overall_score"),
    ("employer_reputation", "qs_overall_score"),
    ("citations_per_faculty", "qs_overall_score"),
    ("faculty_student", "qs_overall_score"),
    ("sustainability", "qs_overall_score"),
    ("international_students", "qs_overall_score")
]

for x, y in scatter_pairs:
    if x in df.columns and y in df.columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[x], y=df[y], alpha=0.6)
        plt.title(f"{x} vs {y}")
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, f"{x}_vs_{y}.png"))
        plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(df["qs_overall_score"], bins=30, kde=True)
plt.title("Overall Score Distribution")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_DIR, "qs_overall_score_distribution.png"))
plt.close()

print("Analysis complete.")
