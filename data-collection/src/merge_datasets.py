# merge_datasets.py

import pandas as pd
import os

# Paths to your raw datasets
fake_path = 'data-collection/data/Fake.csv'
real_path = 'data-collection/data/True.csv'

# Load them
fake_df = pd.read_csv(fake_path)
real_df = pd.read_csv(real_path)

# Add labels
fake_df['label'] = 'FAKE'
real_df['label'] = 'REAL'

# Keep only the columns we need: title and text
fake_df = fake_df[['title', 'text', 'label']]
real_df = real_df[['title', 'text', 'label']]

# Combine and shuffle
combined_df = pd.concat([fake_df, real_df], ignore_index=True).sample(frac=1, random_state=42)

# Create output directory if needed
os.makedirs('data-collection/data', exist_ok=True)

# Save merged CSV
output_path = 'data-collection/data/merged_news.csv'
combined_df.to_csv(output_path, index=False)
print(f"Merged dataset saved to {output_path}")
print(combined_df['label'].value_counts())
