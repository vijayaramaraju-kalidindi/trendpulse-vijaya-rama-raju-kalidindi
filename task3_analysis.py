# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Step 1: Load Cleaned Data
# ---------------------------------------------------------

# Load processed dataset from Task-2
df = pd.read_csv('hacker_news_stories.csv')

# ---------------------------------------------------------
# Step 2: Basic Statistical Analysis
# ---------------------------------------------------------

# Calculate average and median score
average_score = np.mean(df['score'])
median_score = np.median(df['score'])

print(f"Average score: {average_score}")
print(f"Median score: {median_score}")

# Determine skewness based on mean vs median
if average_score > median_score:
    print("Insight: The distribution of scores is right-skewed.")
elif average_score < median_score:
    print("Insight: The distribution of scores is left-skewed.")
else:
    print("Insight: The distribution of scores is symmetric.")

# ---------------------------------------------------------
# Step 3: Top Authors Analysis
# ---------------------------------------------------------

# Identify top 5 authors based on number of posts
top_authors = df['by'].value_counts().head(5)

# Clean index name for better display
top_authors.index.name = None
print(f"\nTop 5 authors:\n{top_authors}")

# ---------------------------------------------------------
# Step 4: Highest Scoring Posts
# ---------------------------------------------------------

# Sort posts by score in descending order and get top 5
highest_score_posts = df.sort_values(by='score', ascending=False).head(5)
print(f"\n Top 5 highest scoring posts:\n {highest_score_posts[['title', 'score']]}")

# ---------------------------------------------------------
# Step 5: Time-Based Analysis
# ---------------------------------------------------------

# Ensure 'time' column is in datetime format
df['time'] = pd.to_datetime(df['time'])

# Extract hour from timestamp
df['hour'] = df['time'].dt.hour

# Count number of posts per hour
hourly_posts = df['hour'].value_counts().sort_index()

print(f"\nNumber of posts by hour of the day:\n{hourly_posts}")