import pandas as pd

# Read CSV file
df = pd.read_csv('stars.csv')

# Perform any necessary transformations on the DataFrame
# For example, you can drop columns, rename columns, filter rows, etc.

# Save DataFrame as Parquet file
df.to_parquet('stars.parquet', index=False)
