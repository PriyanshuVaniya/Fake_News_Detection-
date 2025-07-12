import pandas as pd

# Load fake news
fake_df = pd.read_csv('data-collection/data/Fake.csv')
fake_df['label'] = 'FAKE'

# Load real news
real_df = pd.read_csv('data-collection/data/True.csv')
real_df['label'] = 'REAL'

# Combine datasets
news_df = pd.concat([fake_df, real_df]).sample(frac=1).reset_index(drop=True)

# Show structure
print(news_df.head())
print(news_df.columns)
print(news_df['label'].value_counts())
