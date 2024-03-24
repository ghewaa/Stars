import pandas as pd

# Read Parquet file
df = pd.read_parquet('stars.parquet')

# Display DataFrame
print(df)