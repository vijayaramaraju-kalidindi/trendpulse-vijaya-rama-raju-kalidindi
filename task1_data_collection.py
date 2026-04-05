# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import requests
import json
import time

# ---------------------------------------------------------
# Configuration Section
# ---------------------------------------------------------

# Base URL for Hacker News API
base_url = "https://hacker-news.firebaseio.com/v0"

# Endpoint to fetch all story IDs
stories_url = f"{base_url}/topstories.json"

# ---------------------------------------------------------
# Step 1: Fetch Story IDs
# ---------------------------------------------------------
stories_id = requests.get(stories_url).json()
print(f"Total stories IDs retrieved: {len(stories_id)}")

# ---------------------------------------------------------
# Step 2: Fetch Individual Story Details
# ---------------------------------------------------------
data = []
for story_id in stories_id[:500]:  
    story_url = f"{base_url}/item/{story_id}.json"
    story_response = requests.get(story_url)
    # Check if request was successful
    if story_response.status_code == 200:
        story_data = story_response.json()
        data.append(story_data)
    else:
        print(f"Error fetching story with ID {story_id}")
     # Sleep to prevent hitting API limits
    time.sleep(0.2)

# ---------------------------------------------------------
# Step 3: Save Data to JSON File
# ---------------------------------------------------------
with open('hacker_news_stories.json', 'w') as file:
    json.dump(data, file, indent=4)

# ---------------------------------------------------------
# Step 4: Final Output / Validation
# ---------------------------------------------------------
print("Data collection complete.")
print(f" Stories saved to 'hacker_news_stories.json'.")

# Print sample record safely
if data:
    print(f"Sample story: {data[0]}")
else:
    print("No data collected.")

