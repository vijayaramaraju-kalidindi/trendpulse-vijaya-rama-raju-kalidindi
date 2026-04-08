# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Step 1: Load and Explore Cleaned Data
# ---------------------------------------------------------

# Load processed dataset from Task-2
df = pd.read_csv('data/trends_cleaned.csv')
print(f"Loaded data: {df.shape}")

# Print the first 5 rows
print(f"\nFirst 5:\n{df.head(5)}")

# Print the shape of the DataFrame (rows and columns)
print(f"\nShape of the DataFrame : {df.shape[0]} rows, {df.shape[1]} columns")

# Print the average score and average num_comments across all stories
avg_score = df['score'].mean()
avg_num_comments = df['num_comments'].mean()
print(f"\nAverage score: {avg_score:.0f}")
print(f"Average number of comments: {avg_num_comments:.0f}")

# ---------------------------------------------------------
# Step 2: Basic Analysis with NumPy
# ---------------------------------------------------------

# mean, median, and standard deviation of score
score_mean = np.mean(df['score'])
score_median = np.median(df['score'])
score_std = np.std(df['score'])
print(f"\n--- NumPy Stats ---")
print(f"Mean score   : {score_mean:.0f}")
print(f"Median score : {score_median:.0f}")
print(f"Std Dev score: {score_std:.0f}")

# highest score and lowest score
max_score = np.max(df['score'])
min_score = np.min(df['score'])
print(f"Max score    : {max_score}")
print(f"Min score    : {min_score}")

# category has the most stories
category_counts = df['category'].value_counts()
most_common_category = category_counts.idxmax()
most_common_count = category_counts.max()
print(f"\nMost stories in: {most_common_category} ({most_common_count} stories)")

# story has the most comments
max_comments = np.max(df['num_comments'])
most_commented_story = df[df['num_comments'] == max_comments]['title'].values[0]
print(f'\nMost commented story: "{most_commented_story}"  — {max_comments} comments')

# ---------------------------------------------------------
# Step 3: Add New Columns
# ---------------------------------------------------------

# Engagement = comments per upvote
df['engagement'] = df['num_comments'] / (df['score'] + 1)

# Popular if score > average score
df['popular'] = df['score'] > avg_score
print(f"\nAdded 'engagement' and 'popular' columns.")

# ---------------------------------------------------------
# Step 4: Save Results
# ---------------------------------------------------------
output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)
print(f"\nSaved to {output_path}\n")