import pandas as pd
import os

# How many csv files are there in the 'output' directory?
csv_count = len([f for f in os.listdir('output') if f.endswith('.csv')])
print(f"Number of CSV files in 'output' directory: {csv_count}")

# How many listings are in each csv file?
for filename in os.listdir('output'):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join('output', filename))
        print(f"{filename}: {len(df)} listings")


