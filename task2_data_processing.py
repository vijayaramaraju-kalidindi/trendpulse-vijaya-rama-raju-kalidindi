# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import pandas as pd
import json

# ---------------------------------------------------------
# Step 1: Load JSON Data
# ---------------------------------------------------------

# Load raw Hacker News data collected from Task-1
with open('hacker_news_top_stories.json', 'r') as f:
    data = json.load(f)

# Convert JSON data into a pandas DataFrame
df = pd.DataFrame(data)

# ---------------------------------------------------------
# Step 2: Select Relevant Columns
# ---------------------------------------------------------

# Keep only necessary columns for analysis
df = df[['title', 'by', 'score', 'time', 'type']]

# ---------------------------------------------------------
# Step 3: Check Missing Values
# ---------------------------------------------------------

# Identify missing/null values in each column
print(f"Missing values in the DataFrame:\n{df.isnull().sum()}")

# ---------------------------------------------------------
# Step 4: Filter Valid Story Records
# ---------------------------------------------------------

# Keep only records where type is 'story'
df = df[df['type'] == 'story']

# Drop rows with missing critical fields
df = df.dropna(subset=['title', 'by', 'score', 'time'])

# ---------------------------------------------------------
# Step 5: Data Type Conversion
# ---------------------------------------------------------

# Ensure author names are treated as strings
df['by'] = df['by'].astype(str)

# Convert score to numeric (invalid values become NaN)
df['score'] = pd.to_numeric(df['score'], errors='coerce')

# Drop rows where conversion failed (NaN values introduced)
df =df.dropna()

# Check data types after conversion
print(df.dtypes)

# ---------------------------------------------------------
# Step 6: Convert Timestamp to Readable Format
# ---------------------------------------------------------

# Convert UNIX timestamp to datetime format
df['time'] = pd.to_datetime(df['time'], unit='s')

# ---------------------------------------------------------
# Step 7: Save Cleaned Data
# ---------------------------------------------------------

# Save processed data to CSV for further analysis
df.to_csv('hacker_news_stories.csv', index=False)

# ---------------------------------------------------------
# Step 8: Final Output / Validation
# ---------------------------------------------------------
print("Data processing complete.")
print("Top stories saved to 'hacker_news_stories.csv'.")

# Print total processed records
print(f"Total stories processed: {len(df)}")

# Display a sample record for verification
if not df.empty:
    print(f"Sample story:\n{df.iloc[0]}")
else:
    print("No data available after processing.")
