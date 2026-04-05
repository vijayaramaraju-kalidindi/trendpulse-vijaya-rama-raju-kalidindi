import requests
import json
import time

base_url = "https://hacker-news.firebaseio.com/v0"

top_stories_url = f"{base_url}/topstories.json"
stories_id = requests.get(top_stories_url).json()
print(f"Total top stories IDs retrieved: {len(stories_id)}")

data = []

for story_id in stories_id[:500]:  
    story_url = f"{base_url}/item/{story_id}.json"
    story_response = requests.get(story_url)
    if story_response.status_code == 200:
        story_data = story_response.json()
        data.append(story_data)
    time.sleep(0.2)

with open('hacker_news_top_stories.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data collection complete. Top stories saved to 'hacker_news_top_stories.json'.")
print(f"Sample story: {data[0]}")

