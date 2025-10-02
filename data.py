import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# 2. Run SQL query (fixed column names)
query = """
SELECT product_name AS product, 
       SUM(units_sold) AS total_qty, 
       SUM(units_sold * unit_price) AS revenue
FROM sales
GROUP BY product_name;
"""

# 3. Load results into pandas DataFrame
df = pd.read_sql_query(query, conn)

# 4. Close connection
conn.close()

# 5. Print DataFrame
print(df)

# 6. Plot simple bar chart
df.plot(kind="bar", x="product", y="revenue", legend=False, figsize=(8,5))
plt.ylabel("Revenue ($)")
plt.title("Revenue by Product")
plt.tight_layout()

# 7. Save chart (optional)
plt.savefig("sales_chart.png", dpi=300)

# 8. Show chart
plt.show()
