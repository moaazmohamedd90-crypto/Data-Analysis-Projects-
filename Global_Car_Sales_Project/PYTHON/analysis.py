import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "DATA"

countries = pd.read_csv(DATA_DIR / "countries.csv")
companies = pd.read_csv(DATA_DIR / "companies.csv")
cars = pd.read_csv(DATA_DIR / "cars.csv")
customers = pd.read_csv(DATA_DIR / "customers.csv")
sales = pd.read_csv(DATA_DIR / "sales.csv")

print("Countries:", countries.shape)
print("Companies:", companies.shape)
print("Cars:", cars.shape)
print("Customers:", customers.shape)
print("Sales:", sales.shape)

total_sales = len(sales)
total_cars_sold = sales["quantity"].sum()
total_revenue = (sales["final_price"] * sales["quantity"]).sum()
average_price = sales["final_price"].mean()

print("\n--- Overall Sales Analysis ---")
print("Total Sales:", total_sales)
print("Total Cars Sold:", total_cars_sold)
print("Total Revenue:", total_revenue)
print("Average Sale Price:", round(average_price, 2))

company_analysis = (
    sales
    .merge(cars, on="car_id")
    .merge(companies, on="company_id")
    .groupby("company_name")
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n--- Sales by Company ---")
print(company_analysis)


country_analysis = (
    sales
    .merge(customers, on="customer_id")
    .merge(countries, on="country_id")
    .groupby(["region", "country_name"])
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n--- Sales by Country ---")
print(country_analysis)


category_fuel_analysis = (
    sales
    .merge(cars, on="car_id")
    .groupby(["category", "fuel_type"])
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum"),
        Average_Sale_Price=("final_price", "mean")
    )
    .sort_values("Total_Revenue", ascending=False)
)

print("\n--- Sales by Category and Fuel Type ---")
print(category_fuel_analysis.round(2))


model_analysis = (
    sales
    .merge(cars, on="car_id")
    .merge(companies, on="company_id")
    .groupby(["company_name", "model"])
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n--- Top Selling Car Models ---")
print(model_analysis.head(15))


yearly_analysis = (
    sales
    .assign(Sale_Year=pd.to_datetime(sales["sale_date"]).dt.year)
    .groupby("Sale_Year")
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum")
    )
    .sort_index()
)

print("\n--- Yearly Sales Analysis ---")
print(yearly_analysis)


model_year_analysis = (
    sales
    .merge(cars, on="car_id")
    .merge(companies, on="company_id")
    .assign(Sale_Year=pd.to_datetime(sales["sale_date"]).dt.year)
    .groupby(["Sale_Year", "company_name", "model"])
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum")
    )
    .sort_values(["Sale_Year", "Total_Sales"], ascending=[True, False])
)

print("\n--- Model Performance by Year ---")
print(model_year_analysis)


customer_analysis = (
    sales
    .merge(customers, on="customer_id")
    .merge(countries, on="country_id")
    .groupby(["customer_id", "customer_name", "country_name"])
    .agg(
        Total_Purchases=("sale_id", "count"),
        Total_Spending=("final_price", "sum")
    )
    .sort_values("Total_Spending", ascending=False)
)

print("\n--- Top 10 Customers ---")
print(customer_analysis.head(10))


region_company_analysis = (
    sales
    .merge(customers, on="customer_id")
    .merge(countries, on="country_id")
    .merge(cars, on="car_id")
    .merge(companies, on="company_id")
    .groupby(["region", "company_name"])
    .agg(
        Total_Sales=("sale_id", "count"),
        Total_Revenue=("final_price", "sum"),
        Average_Discount=("discount_percent", "mean")
    )
    .sort_values("Total_Revenue", ascending=False)
)

region_company_analysis["Average_Discount"] = (
    region_company_analysis["Average_Discount"].round(2)
)

print("\n--- Company Performance by Region ---")
print(region_company_analysis)

print("\n--- Missing Values ---")
print(sales.isnull().sum())

print("\n--- Duplicate Rows ---")
print(sales.duplicated().sum())

print("\n--- Data Types ---")
print(sales.dtypes)


print("\n--- Data Validation ---")

print("Age range:", customers["age"].min(), "to", customers["age"].max())
print("Discount range:", sales["discount_percent"].min(), "to", sales["discount_percent"].max())
print("Quantity values:", sales["quantity"].unique())
print("Negative prices:", (sales["final_price"] < 0).sum())

sales["sale_date"] = pd.to_datetime(sales["sale_date"])

print("\n--- Updated Data Types ---")
print(sales.dtypes)

sales["Sale_Year"] = sales["sale_date"].dt.year
sales["Sale_Month"] = sales["sale_date"].dt.month
sales["Sale_Quarter"] = sales["sale_date"].dt.quarter

print("\n--- New Features ---")
print(sales[["sale_date", "Sale_Year", "Sale_Month", "Sale_Quarter"]].head(10))

