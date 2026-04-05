import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hacker_news_top_stories.csv')

df['time'] = pd.to_datetime(df['time'])
df['hour'] = df['time'].dt.hour
df['title_length'] = df['title'].apply(len)

top_authors = df['by'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_authors.plot(kind='bar')
plt.title('Top 10 Authors by Number of Posts')
plt.xlabel('Author')
plt.ylabel('Number of Posts')
plt.xticks(rotation=45)
plt.tight_layout()


plt.figure(figsize=(10, 6))
df['score'].plot(kind='hist', bins=30, edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.tight_layout()


plt.figure(figsize=(10, 6))
hourly_posts = df['hour'].value_counts().sort_index()
hourly_posts.plot(kind='line', marker='o')
plt.title('Hourly Posts')
plt.xlabel('Hour')
plt.ylabel('Number of Posts')
plt.tight_layout()

top_posts = df.sort_values(by='score', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_posts['title'], top_posts['score'], color='skyblue')
plt.title('Top 10 Highest Scoring Posts')
plt.xlabel('Score') 
plt.ylabel('Post Title')
plt.gca().invert_yaxis()
plt.yticks(fontsize=8)
plt.tight_layout()


plt.figure(figsize=(10, 6))
plt.scatter(df['title_length'], df['score'], alpha=0.5)
plt.title('Title Length vs. Score')
plt.xlabel('Title Length')
plt.ylabel('Score')
plt.tight_layout()


plt.figure(figsize=(10, 6))
plt.boxplot(df['score'])
plt.title('Box Plot of Scores')
plt.xlabel('Score')
plt.tight_layout() 

plt.figure(figsize=(10, 6))
top_authors = df['by'].value_counts().head(5)
explode = [0.1] + [0]*4
plt.pie(top_authors, labels=top_authors.index, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title('Top 5 Authors by Number of Posts')
plt.tight_layout()
plt.show()