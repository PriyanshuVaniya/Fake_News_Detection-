import pandas as pd
import re
from sklearn.model_selection import train_test_split

def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    text = text.lower()
    return text

def load_and_preprocess(path):
    df = pd.read_csv(path)
    df = df[['title', 'text', 'label']]
    df['text'] = df['text'].fillna('')
    df['combined'] = df['title'] + " " + df['text']
    df['combined'] = df['combined'].apply(clean_text)
    return df

if __name__ == "__main__":
    df = load_and_preprocess('data-collection/data/merged_news.csv')  # change if needed
    print(df.head())
