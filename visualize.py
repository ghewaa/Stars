import pandas as pd
import matplotlib.pyplot as plt


# Read Parquet file
df = pd.read_parquet('stars.parquet')

# Count the frequency of each star color
color_counts = df['Star color'].value_counts()

# Plot bar chart
color_counts.plot(kind='bar')
plt.xlabel('Star Color')
plt.ylabel('Frequency')
plt.title('Distribution of Star Colors')
plt.show()

plt.savefig('star_color_distribution.png')  # Save the plot to a file
