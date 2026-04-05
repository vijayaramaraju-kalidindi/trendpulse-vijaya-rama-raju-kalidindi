# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# Step 1: Load Processed Data
# ---------------------------------------------------------

# Load cleaned dataset generated from Task-2
df = pd.read_csv('hacker_news_stories.csv')

# ---------------------------------------------------------
# Step 2: Feature Engineering
# ---------------------------------------------------------

# Convert 'time' column to datetime format
df['time'] = pd.to_datetime(df['time'])
# Extract hour of the day for time-based analysis
df['hour'] = df['time'].dt.hour
# Create a new feature: length of title (number of characters)
df['title_length'] = df['title'].apply(len)

# ---------------------------------------------------------
# Step 3: Top Authors (Bar Chart)
# ---------------------------------------------------------

# Identify top 10 authors based on number of posts
top_authors = df['by'].value_counts().head(10)
plt.figure(figsize=(10, 6))
# Bar chart showing most active authors
top_authors.plot(kind='bar')
plt.title('Top 10 Authors by Number of Posts')
plt.xlabel('Author')
plt.ylabel('Number of Posts')
plt.xticks(rotation=45)
# Adjust layout to prevent label overlap
plt.tight_layout()

# ---------------------------------------------------------
# Step 4: Score Distribution (Histogram)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
# Histogram to understand distribution of scores
df['score'].plot(kind='hist', bins=30, edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.tight_layout()

# ---------------------------------------------------------
# Step 5: Posting Activity by Hour (Line Plot)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
# Count number of posts for each hour
hourly_posts = df['hour'].value_counts().sort_index()
# Line plot to show posting trend over 24 hours
hourly_posts.plot(kind='line', marker='o')
plt.title('Hourly Posts')
plt.xlabel('Hour')
plt.ylabel('Number of Posts')
plt.tight_layout()

# ---------------------------------------------------------
# Step 6: Top Scoring Posts (Horizontal Bar Chart)
# ---------------------------------------------------------

# Get top 10 highest scoring posts
top_posts = df.sort_values(by='score', ascending=False).head(10)
plt.figure(figsize=(10, 6))
# Horizontal bar chart for better readability of long titles
plt.barh(top_posts['title'], top_posts['score'], color='skyblue')
plt.title('Top 10 Highest Scoring Posts')
plt.xlabel('Score') 
plt.ylabel('Post Title')
# Invert y-axis so highest score appears on top
plt.gca().invert_yaxis()
# Reduce font size to fit long titles
plt.yticks(fontsize=8)
plt.tight_layout()

# ---------------------------------------------------------
# Step 7: Title Length vs Score (Scatter Plot)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
# Scatter plot to analyze relationship between title length and score
plt.scatter(df['title_length'], df['score'], alpha=0.5)
plt.title('Title Length vs. Score')
plt.xlabel('Title Length')
plt.ylabel('Score')
plt.tight_layout()

# ---------------------------------------------------------
# Step 8: Score Distribution (Seaborn Box Plot)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
# Box plot to visualize spread, median, and outliers in scores
sns.boxplot(x=df['score'])
plt.title('Box Plot of Scores')
plt.xlabel('Score')
plt.tight_layout()

# ---------------------------------------------------------
# Step 9: Top Authors Contribution (Pie Chart)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
# Top 5 authors for proportional comparison
top_authors = df['by'].value_counts().head(5)
# Highlight the top contributor
explode = [0.1] + [0]*4
# Pie chart showing contribution percentage
plt.pie(top_authors, labels=top_authors.index, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title('Top 5 Authors by Number of Posts')
plt.tight_layout()

# ---------------------------------------------------------
# Step 10: Display All Plots
# ---------------------------------------------------------

# Render all visualizations
plt.show()