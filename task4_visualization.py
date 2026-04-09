# ---------------------------------------------------------
# Step 0: Import Required Libraries
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import textwrap

# ---------------------------------------------------------
# Step 1: Load Processed Data
# ---------------------------------------------------------

# Load cleaned dataset generated from Task-3
df = pd.read_csv('data/trends_analysed.csv')

# Create outputs folder if not exists
os.makedirs('outputs', exist_ok=True)


# create a function to shorten long titles for better visualization
def wrap_title(title, width=50):
    return "\n".join(textwrap.wrap(title, width))

# ---------------------------------------------------------
# Step 2: Chart 1: Top 10 Stories by Score
# ---------------------------------------------------------
top_10_stories = df.sort_values(by='score', ascending=False).head(10)
titles = top_10_stories['title'].apply(wrap_title)
scores = top_10_stories['score']
plt.figure(figsize=(10, 6))
plt.barh(titles, scores, color='skyblue')
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.title('Top 10 Stories by Score')
plt.gca().invert_yaxis() 
plt.tight_layout()
plt.subplots_adjust(left=0.4)
plt.savefig('outputs/chart1_top_stories.png', dpi=300, bbox_inches='tight')
plt.show()

# ---------------------------------------------------------
# Step 3: Chart 2: Stories per Category
# ---------------------------------------------------------
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta']
category_counts = df['category'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(category_counts.index, category_counts.values, color=colors, width=0.4)
plt.xlabel('Category')
plt.ylabel('Number of Stories')
plt.title('Stories per Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/chart2_categories.png', dpi=300, bbox_inches='tight')
plt.show()

# ---------------------------------------------------------
# Step 4: Chart 3: Score vs Comments: Chart 2: Stories per Category
# ---------------------------------------------------------
popular = df[df['popular'] == True]
not_popular = df[df['popular'] == False]
plt.figure(figsize=(10, 6))
plt.scatter(popular['score'], popular['num_comments'], label='Popular')
plt.scatter(not_popular['score'], not_popular['num_comments'], label='Not Popular')
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.tight_layout()
plt.savefig('outputs/chart3_scatter.png')
plt.show()

# ---------------------------------------------------------
# Step 5: Dashboard  
# ---------------------------------------------------------

# Combine all 3 charts
fig, axes = plt.subplots(1, 3, figsize=(18,5))
fig.subplots_adjust(left=0.35, wspace=0.4)

#chart-1
axes[0].barh(titles, scores)
axes[0].set_title("Top 10 Stories by Score")
axes[0].invert_yaxis()
#chart-2
axes[1].bar(category_counts.index, category_counts.values, color=colors)
axes[1].set_title("Stories per Category")
axes[1].tick_params(axis='x', rotation=45)
#chart-3
axes[2].scatter(popular['score'], popular['num_comments'], label='Popular')
axes[2].scatter(not_popular['score'], not_popular['num_comments'], label='Not Popular')
axes[2].set_title("Score vs Comments")
axes[2].legend()
fig.suptitle("TrendPulse Dashboard")
plt.tight_layout()
plt.savefig('outputs/dashboard.png')
plt.show()