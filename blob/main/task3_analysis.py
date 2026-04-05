import pandas as pd
import numpy as np

df = pd.read_csv('hacker_news_top_stories.csv')

average_score = np.mean(df['score'])
median_score = np.median(df['score'])

print(f"Average score: {average_score}")
print(f"Median score: {median_score}")

if average_score > median_score:
    print("Insight: The distribution of scores is right-skewed.")
else:
    print("The distribution is fairly balanced or left-skewed.")

top_authors = df['by'].value_counts().head(5)
top_authors.index.name = None
print(f"\nTop 5 authors:\n{top_authors}")

highest_score_posts = df.sort_values(by='score', ascending=False).head(5)
print(f"\n Top 5 highest scoring posts:\n {highest_score_posts[['title', 'score']]}")

df['time'] = pd.to_datetime(df['time'])
df['hour'] = df['time'].dt.hour

hourly_posts = df['hour'].value_counts().sort_index()

print(f"\nNumber of posts by hour of the day:\n{hourly_posts}")