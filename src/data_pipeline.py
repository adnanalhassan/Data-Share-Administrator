import pandas as pd

# Load raw data
scores = pd.read_csv("data/exam_scores.csv")
meta = pd.read_csv("data/student_metadata.csv")

# Merge datasets on student_id
merged = pd.merge(scores, meta, on="student_id", how="inner")

# Drop any rows with missing or unrealistic values
cleaned = merged.dropna()
cleaned = cleaned[cleaned["exam_score"].between(0, 100)]

# Anonymize student names
cleaned["student_name"] = "ANON"

# Save cleaned dataset
cleaned.to_csv("output/cleaned_dataset.csv", index=False)
print("✅ Cleaned dataset saved.")
