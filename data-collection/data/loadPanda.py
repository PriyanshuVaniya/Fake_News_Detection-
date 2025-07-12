import pandas as pd

csv_file = "C:/Dump/data.csv"  # Update this path
df = pd.read_csv(csv_file)

print(df.head())  # Show the first 5 rows
print(df.columns)  # Display column names

json_file = "C:/Dump/News_Category_Dataset_v3.json"  # Update this path
df_json = pd.read_json(json_file, lines=True)  # Use `lines=True` if it's in JSONL format

print(df_json.head())  # Show the first 5 rows
print(df_json.columns)
