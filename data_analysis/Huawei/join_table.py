import pandas as pd

# Read each CSV file
mate50_df = pd.read_csv("Huawei_mate50.csv")
mate60_df = pd.read_csv("Huawei_mate60.csv")
p60_df = pd.read_csv("Huawei_p60.csv")

# Add 'model' column
mate50_df['model'] = 'Mate 50'
mate60_df['model'] = 'Mate 60'
p60_df['model'] = 'P60'

# Merge all dataframes into one
merged_df = pd.concat([mate50_df, mate60_df, p60_df], ignore_index=True)
merged_df = merged_df[(merged_df['price'] >= 1000) & (merged_df['realSales'] >= 10) & (merged_df['Charging Power'].notnull()) & (merged_df['Charging Power'] != 0) & (merged_df['Camera Pixel'].notnull())]

# Define a custom function to apply different multiplication factors
# Apply the custom function to the 'realSales' column
merged_df['realSales'] = merged_df['realSales'] * 12

sorted_df = merged_df.sort_values(by='realSales', ascending=False)

# Select the top 100 rows
top_100_df = sorted_df.head(100)

# Save the top 100 rows to a new CSV file
top_100_df.to_csv("merged_huawei_data.csv", index=False)
