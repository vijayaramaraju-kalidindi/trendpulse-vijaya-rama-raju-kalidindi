import pandas as pd
import json

with open('hacker_news_top_stories.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df = df[['title', 'by', 'score', 'time', 'type']]
print(f"Missing values in the DataFrame:\n{df.isnull().sum()}")
df = df[df['type'] == 'story']
df = df.dropna(subset=['title', 'by', 'score', 'time'])

df['by'] = df['by'].astype(str)
df['score'] = pd.to_numeric(df['score'], errors='coerce')

df =df.dropna()
print(df.dtypes)

df['time'] = pd.to_datetime(df['time'], unit='s')
df.to_csv('hacker_news_top_stories.csv', index=False)
print("Data processing complete. Top stories saved to 'hacker_news_top_stories.csv'.")
print(f"Total stories processed: {len(df)}")
print(f"Sample story:\n{df.iloc[0]}")
