# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import pandas as pd
import json

# ---------------------------------------------------------
# Step 1: Load JSON Data
# ---------------------------------------------------------

# Load category filtered Hacker News data collected from Task-1

file_path = "data/trends_20260408.json" 
df = pd.read_json(file_path)
print(f"Loaded {len(df)} stories from {file_path}")

## Temporary loading df data to csv to check for duplicates and missing values before cleaning.
temp_path = "data/trends_before_cleaning.csv"
df.to_csv(temp_path, index=False)

# ---------------------------------------------------------
# Step 2: Clean the Data
# ---------------------------------------------------------

# 1. Remove duplicates based on post_id
df = df.drop_duplicates(subset='post_id')
print(f"\nAfter removing duplicates: {len(df)}")

# 2. Remove missing values
df = df.dropna(subset=['post_id', 'title', 'score'])
print(f"After removing nulls: {len(df)}")

# 3. Data types — make sure score and num_comments are integers
df['score'] = pd.to_numeric(df['score'], errors='coerce')
df['num_comments'] = pd.to_numeric(df['num_comments'], errors='coerce')
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

# 4. Remove low-quality stories (score < 5)
df = df[df['score'] >= 5]
print(f"After removing low scores: {len(df)}")

# 5. Strip whitespace from title
df['title'] = df['title'].str.strip()

# Print the number of rows remaining after cleaning.
print(f"\nNumber of rows after cleaning: {len(df)}")

# ---------------------------------------------------------
# Step 3: Save as CSV
# ---------------------------------------------------------
output_path = "data/trends_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\nSaved {len(df)} rows to {output_path}")

# ---------------------------------------------------------
# Step 4: Stories per category
# ---------------------------------------------------------
print("\nStories per category:")
category_counts = df['category'].value_counts()

for cat, count in category_counts.items():
    print(f"  {cat}: {count}")
