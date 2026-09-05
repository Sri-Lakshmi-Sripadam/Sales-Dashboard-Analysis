# Sales Dashboard Analysis - Python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Superstore.csv')  # nee dataset name

# Basic KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Total Profit: ${total_profit:,.0f}")

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(region_sales)

# Profit Margin by Category
category_profit = df.groupby('Category')['Profit'].mean()
print("\nProfit by Category:")
print(category_profit)

# Discount vs Loss Analysis
loss_orders = df[df['Profit'] < 0]
high_discount_loss = loss_orders[loss_orders['Discount'] > 0.25]
print(f"\nLoss due to high discount: {len(high_discount_loss)} orders")
