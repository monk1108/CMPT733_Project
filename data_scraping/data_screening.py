import pandas as pd

# Read the CSV file
df = pd.read_csv("iPhone/iPhone.csv")

# Filter the dataframe based on conditions
df = df[(df['price'] >= 1000) & (df['realSales'] >= 100) & (df['Charging Power'].notnull()) & (df['Charging Power'] != 0) & (df['Camera Pixel'].notnull())]

# Save the filtered dataframe to a new CSV file
df.to_csv("new_iPhone.csv", index=False)
