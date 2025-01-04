import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Compute the total sales
df['Total_Sales'] = df['Quantity'] * df['Price']

# Create a pivot table (Data Cube) with multi-dimensional aggregation
data_cube = pd.pivot_table(df, values='Total_Sales', index=['Region', 'Product'], columns=['Month'], aggfunc='sum', fill_value=0)
print("Data Cube:")
print(data_cube)

# Save the data cube to a CSV file
data_cube.to_csv('data_cube.csv')


# Load the data cube
data_cube = pd.read_csv('data_cube.csv')

# Set the correct index
data_cube.set_index(['Region', 'Product'], inplace=True)
print("\nLoaded Data Cube:")
print(data_cube)

# Query 1: Total sales for a specific product across all regions and months
product_total_sales = data_cube.xs('Widget', level='Product').sum(axis=1)
print("\nTotal Sales for 'Widget' across all regions and months:")
print(product_total_sales)

# Query 2: Total sales for a specific region across all products and months
region_total_sales = data_cube.xs('North', level='Region').sum(axis=1)
print("\nTotal Sales in 'North' region across all products and months:")
print(region_total_sales)

# Query 3: Total sales in a specific month across all regions and products
month_total_sales = data_cube.sum(axis=0).loc['January']
print("\nTotal Sales in 'January' across all regions and products:")
print(month_total_sales)



