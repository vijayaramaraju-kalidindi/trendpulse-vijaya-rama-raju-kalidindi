# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import requests
import json
import time
import os
from datetime import datetime

# ---------------------------------------------------------
# Configuration Section
# ---------------------------------------------------------

# Base URL for Hacker News API
base_url = "https://hacker-news.firebaseio.com/v0"
stories_url = f"{base_url}/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

# ---------------------------------------------------------
# Category Mapping
# ---------------------------------------------------------
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

max_per_category = 25

# ---------------------------------------------------------
# Function: Categorize Story
# ---------------------------------------------------------
def categorize_story(title):
    if not title:
        return None
    title_lower = title.lower()
    for category, keywords in categories.items():
        if any(keyword in title_lower for keyword in keywords):
            return category
    return None

# ---------------------------------------------------------
# Step 1: Fetch Story IDs
# ---------------------------------------------------------
response = requests.get(stories_url, headers=headers)
if response.status_code != 200:
    raise Exception("Failed to fetch story IDs from Hacker News API.")

stories_id = response.json()
print(f"Total story IDs retrieved: {len(stories_id)}")  

# ---------------------------------------------------------
# Step 2: Fetch Individual Story Details
# ---------------------------------------------------------
collected = {cat: [] for cat in categories}
for story_id in stories_id[:500]:  
    story_url = f"{base_url}/item/{story_id}.json"
    try: 
        res = requests.get(story_url, headers=headers)
        if res.status_code != 200:
            print(f"Failed to fetch story with ID {story_id}. Status code: {res.status_code}")
            continue
        story_data = res.json()
        if not story_data or "title" not in story_data:
            continue
        category = categorize_story(story_data.get("title"))
        # Only proceed if category matches AND not full    
        if category and len(collected[category]) < max_per_category:
                processed_story = {
                    "post_id": story_data.get("id"),
                    "title": story_data.get("title"),
                    "category": category,
                    "score": story_data.get("score", 0),
                    "num_comments": story_data.get("descendants", 0),
                    "author": story_data.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                collected[category].append(processed_story)
        # Sleep when category reaches 25
        if category and category in collected:
           if len(collected[category]) == max_per_category:
            print(f"{category} completed ({max_per_category} stories). Sleeping 2 seconds")
            time.sleep(2)
        
        if all(len(v) == max_per_category for v in collected.values()):
           break
    except Exception as e:
                print(f"Error fetching story with ID {story_id}: {e}")
# ---------------------------------------------------------
# Step 3: Flatten Data
# ---------------------------------------------------------
final_data = []
for category_list in collected.values():
    final_data.extend(category_list)

# ---------------------------------------------------------
# Step 4: Save Data to JSON File
# ---------------------------------------------------------
os.makedirs('data', exist_ok=True)  # Create 'data' directory if it doesn't exist
filename = f"data/trends_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, 'w') as file:
    json.dump(final_data, file, indent=4)

# ---------------------------------------------------------
# Step 5: Final Output / Validation
# ---------------------------------------------------------
print("Data collection complete.")
print(f"Collected {len(final_data)} stories.")
print(f"Data saved to: {filename}")

print("\nCategory counts:")
for cat, items in collected.items():
    print(f"{cat}: {len(items)}")

# Print sample record safely
if final_data:
    print("\nSample Record:")
    print(json.dumps(final_data[0], indent=2))

