import pandas as pd
import matplotlib.pyplot as plt

pf = pd.read_csv("sales_dataset.csv")

pf["Total Sales"] = pf["Quantity"] * pf["Unit Price"]

print("Cleaned sales dataset: \n")
print(pf.head())

print("\nDataset Info:")
print(pf.info())

print("\nBasic Statistics:")
print(pf.describe())

plt.style.use('ggplot')

# 1. Line Chart: Sales Trend Over Time
plt.figure(figsize=(10, 5))
pf.groupby("Date")["Total Sales"].sum().plot(kind="line", marker="o")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart: Average Sales per Product
avg_sales_per_product = pf.groupby("Product")["Total Sales"].mean()

plt.figure(figsize=(8, 5))
avg_sales_per_product.plot(kind="bar", color="skyblue")
plt.title("Average Total Sales per Product")
plt.xlabel("Product")
plt.ylabel("Average Sales")
plt.xticks(rotation=45)
plt.show()

# 3. Histogram: Distribution of Unit Price
plt.figure(figsize=(8, 5))
plt.hist(pf['Unit Price'], bins=10, color="orange", edgecolor="black")
plt.title("Distribution of Unit Prices")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Quantity vs Total Sales
plt.figure(figsize=(8, 5))
plt.scatter(pf['Quantity'], pf['Total Sales'], alpha=0.7, color="green")
plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.show()
