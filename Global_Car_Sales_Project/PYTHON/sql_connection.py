import pyodbc
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
EXCEL_DIR = BASE_DIR / "EXCEL"


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER= DESKTOP-J6AB4GV\\SQLEXPRESS;"
    "DATABASE=GlobalCarSales;"
    "Trusted_Connection=yes;"
)

print("Connected successfully!")

query = """
SELECT TOP 10 *
FROM Sales
"""

sales = pd.read_sql(query, conn)

print(sales)

query = """
SELECT
    COUNT(*) AS Total_Sales,
    SUM(quantity) AS Total_Cars_Sold,
    SUM(final_price * quantity) AS Total_Revenue,
    AVG(final_price) AS Average_Sale_Price
FROM Sales
"""

result = pd.read_sql(query, conn)

print("\n--- Overall Sales Analysis ---")
print(result)

query_company = """
SELECT
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name
ORDER BY Total_Revenue DESC
"""

company_sales = pd.read_sql(query_company, conn)

print("\n--- Sales by Company ---")
print(company_sales)


query_country = """
SELECT
    co.country_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
GROUP BY co.country_name
ORDER BY Total_Revenue DESC
"""

country_sales = pd.read_sql(query_country, conn)

print("\n--- Sales by Country ---")
print(country_sales)


query_category = """
SELECT
    ca.category,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.category
ORDER BY Total_Revenue DESC
"""

category_sales = pd.read_sql(query_category, conn)

print("\n--- Sales by Category ---")
print(category_sales)


query_fuel = """
SELECT
    ca.fuel_type,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.fuel_type
ORDER BY Total_Revenue DESC
"""

fuel_sales = pd.read_sql(query_fuel, conn)

print("\n--- Sales by Fuel Type ---")
print(fuel_sales)


query_models = """
SELECT TOP 10
    ca.model,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY ca.model, c.company_name
ORDER BY Total_Sales DESC
"""

top_models = pd.read_sql(query_models, conn)

print("\n--- Top 10 Best-Selling Car Models ---")
print(top_models)


query_year = """
SELECT
    YEAR(s.sale_date) AS Sale_Year,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
GROUP BY YEAR(s.sale_date)
ORDER BY Sale_Year
"""

yearly_sales = pd.read_sql(query_year, conn)

print("\n--- Yearly Sales Analysis ---")
print(yearly_sales)


query_discount = """
SELECT
    c.company_name,
    AVG(s.discount_percent) AS Average_Discount,
    COUNT(s.sale_id) AS Total_Sales
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name
ORDER BY Average_Discount DESC
"""

discount_analysis = pd.read_sql(query_discount, conn)

print("\n--- Average Discount by Company ---")
print(discount_analysis.round(2))


query_customers = """
SELECT TOP 10
    cu.customer_id,
    cu.customer_name,
    co.country_name,
    COUNT(s.sale_id) AS Total_Purchases,
    SUM(s.final_price * s.quantity) AS Total_Spending
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
GROUP BY cu.customer_id, cu.customer_name, co.country_name
ORDER BY Total_Spending DESC
"""

top_customers = pd.read_sql(query_customers, conn)

print("\n--- Top 10 Customers ---")
print(top_customers)


query_region_company = """
SELECT
    co.region,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue,
    AVG(s.discount_percent) AS Average_Discount
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY co.region, c.company_name
ORDER BY co.region, Total_Revenue DESC
"""

region_company = pd.read_sql(query_region_company, conn)

region_company["Average_Discount"] = region_company["Average_Discount"].round(2)

print("\n--- Company Performance by Region ---")
print(region_company)

query_model_year = """
SELECT
    YEAR(s.sale_date) AS Sale_Year,
    co.region,
    c.company_name,
    ca.model,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY
    YEAR(s.sale_date),
    co.region,
    c.company_name,
    ca.model
ORDER BY
    Sale_Year,
    co.region,
    Total_Sales DESC
"""

model_year = pd.read_sql(query_model_year, conn)

print("\n--- Model Performance by Year ---")
print(model_year)

with pd.ExcelWriter(EXCEL_DIR / "Global_Car_Sales_Analysis.xlsx") as writer:
    result.to_excel(writer, sheet_name="Overall_Sales_Analysis", index=False)
    company_sales.to_excel(writer, sheet_name="Sales_by_Company", index=False)
    country_sales.to_excel(writer, sheet_name="Sales_by_Country", index=False)
    category_sales.to_excel(writer, sheet_name="Sales_by_Category", index=False)
    fuel_sales.to_excel(writer, sheet_name="Sales_by_Fuel_Type", index=False)
    top_models.to_excel(writer, sheet_name="Top_10_Best_Selling_Models", index=False)
    yearly_sales.to_excel(writer, sheet_name="Yearly_Sales_Analysis", index=False)
    discount_analysis.to_excel(writer, sheet_name="Average_Discount_by_Company", index=False)
    top_customers.to_excel(writer, sheet_name="Top_10_Customers", index=False)
    region_company.to_excel(writer, sheet_name="Company_Performance_by_Region", index=False)
    model_year.to_excel(writer, sheet_name="Model_Performance_by_Year", index=False)