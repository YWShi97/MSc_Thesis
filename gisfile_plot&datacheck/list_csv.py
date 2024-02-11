# This code is used to list the csv data.

import pandas as pd

# Path to CSV file
csv_file_path = r'C:\Users\yuwei\Desktop\Afterprocess\Technical Sector\Final area\Masked_MWD_data.csv'

# Read CSV file
df = pd.read_csv(csv_file_path)

# Print the column names
print(df.columns)
