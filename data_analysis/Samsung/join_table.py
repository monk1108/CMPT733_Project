import pandas as pd

# Read each CSV file
Samsung_s22_df = pd.read_csv("Samsung_s22.csv")
Samsung_s23_df = pd.read_csv("Samsung_s23.csv")
Samsung_s24_df = pd.read_csv("Samsung_s24.csv")
Samsung_z_df = pd.read_csv("Samsung_z.csv")

# Add 'model' column
Samsung_s22_df['model'] = 'Samsung S22'
Samsung_s23_df['model'] = 'Samsung S23'
Samsung_s24_df['model'] = 'Samsung S24'
Samsung_z_df['model'] = 'Samsung z'

# Merge all dataframes into one
merged_df = pd.concat([Samsung_s22_df, Samsung_s23_df, Samsung_s24_df, Samsung_z_df], ignore_index=True)

merged_df = merged_df[(merged_df['price'] >= 1000) & (merged_df['realSales'] >= 10) & (merged_df['Charging Power'].notnull()) & (merged_df['Charging Power'] != 0) & (merged_df['Camera Pixel'].notnull())]

# Define a custom function to apply different multiplication factors
# Apply the custom function to the 'realSales' column
merged_df['realSales'] = merged_df['realSales'] * 12

sorted_df = merged_df.sort_values(by='realSales', ascending=False)

# Select the top 100 rows
top_100_df = sorted_df.head(100)

# Save the top 100 rows to a new CSV file
top_100_df.to_csv("merged_samsung_data.csv", index=False)