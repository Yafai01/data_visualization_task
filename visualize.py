import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("data/Superstore.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df = df.dropna(subset=['Order Date'])

monthly = df.set_index('Order Date').resample('M').agg({'Sales':'sum','Profit':'sum'}).reset_index()
categories = df.groupby('Category').agg({'Sales':'sum','Profit':'sum'}).reset_index()

# Chart 1 - Monthly Sales
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly, x='Order Date', y='Sales')
plt.title('Monthly Sales Trend')
plt.tight_layout()
plt.savefig('outputs/monthly_sales.png', dpi=150)
plt.close()

# Chart 2 - Category Sales
plt.figure(figsize=(8,5))
sns.barplot(data=categories.sort_values('Sales',ascending=False), x='Category', y='Sales')
plt.title('Sales by Category')
plt.tight_layout()
plt.savefig('outputs/category_sales.png', dpi=150)
plt.close()

# Chart 3 - Interactive Chart
fig = px.treemap(categories, path=['Category'], values='Sales', title='Category Sales Treemap')
fig.write_image('outputs/category_treemap.png')

print("?? Visualization Complete! Check the outputs folder.")
