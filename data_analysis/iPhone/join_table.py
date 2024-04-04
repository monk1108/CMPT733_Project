import pandas as pd

# Read each CSV file
iphone12_df = pd.read_csv("iPhone12.csv")
iphone13_df = pd.read_csv("iPhone13.csv")
iphone14_df = pd.read_csv("iPhone14.csv")
iphone15_df = pd.read_csv("iPhone15.csv")

# Add 'model' column
iphone12_df['model'] = '12'
iphone13_df['model'] = '13'
iphone14_df['model'] = '14'
iphone15_df['model'] = '15'

# Merge all dataframes into one
merged_df = pd.concat([iphone12_df, iphone13_df, iphone14_df, iphone15_df], ignore_index=True)
merged_df = merged_df[(merged_df['price'] >= 1000) & (merged_df['realSales'] >= 10) & (merged_df['Charging Power'].notnull()) & (merged_df['Charging Power'] != 0) & (merged_df['Camera Pixel'].notnull())]

# Define a custom function to apply different multiplication factors
# def multiply_sales(row):
#     if row['realSales'] <= 1000:
#         return row['realSales'] * 15
#     else:
#         return row['realSales'] * 5

# Apply the custom function to the 'realSales' column
merged_df['realSales'] = merged_df['realSales'] * 12

sorted_df = merged_df.sort_values(by='realSales', ascending=False)

# Select the top 100 rows
top_100_df = sorted_df.head(100)

# Save the top 100 rows to a new CSV file
top_100_df.to_csv("merged_iphone_data.csv", index=False)
