import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

def run_munging():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE_PATH = os.path.join(BASE_DIR, "datasets", "qs_world_rankings_2025.csv")

    df = pd.read_csv(FILE_PATH, sep=None, engine="python")

    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace("-", "_")
    )

    numeric_cols = [
        "rank",
        "overall_score",
        "academic_reputation",
        "employer_reputation",
        "citations_per_faculty",
        "faculty_student_ratio",
        "international_faculty_ratio",
        "international_student_ratio",
        "sustainability_score"
    ]

    numeric_cols = [col for col in numeric_cols if col in df.columns]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[numeric_cols])
    scaled_df = pd.DataFrame(scaled, columns=[f"{c}_scaled" for c in numeric_cols])

    df = pd.concat([df.reset_index(drop=True), scaled_df.reset_index(drop=True)], axis=1)

    OUTPUT_PATH = os.path.join(BASE_DIR, "datasets", "qs_data_cleaned.csv")
    df.to_csv(OUTPUT_PATH, index=False)

    print(df.head())

if __name__ == "__main__":
    run_munging()
