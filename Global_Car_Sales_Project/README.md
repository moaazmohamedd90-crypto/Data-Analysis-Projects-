# Global Car Sales Analytics

## Project Overview

Global Car Sales Analytics is an end-to-end data analytics project that analyzes car sales across different countries, regions, companies, categories, fuel types, and car models.

The project demonstrates the complete data analytics workflow from data generation and database design to SQL analysis, Python analysis, Excel reporting, and Power BI visualization.

## Data Description

The dataset is synthetically generated for educational and analytical purposes.

The project uses realistic car company and model names, while customer and sales records are generated programmatically.

The dataset contains:

- 54 countries
- 45 car companies
- 151 car models
- 2,000 customers
- 10,000 sales transactions

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Faker
- PyODBC
- Microsoft SQL Server
- SQL Server Management Studio (SSMS)
- Microsoft Excel
- Power BI

## Database Structure

The SQL Server database is named:

`GlobalCarSales`

It contains five related tables:

- Countries
- Companies
- Cars
- Customers
- Sales

### Main Relationships

- Countries → Customers
- Companies → Cars
- Customers → Sales
- Cars → Sales

Primary Keys and Foreign Keys are used to maintain relationships between the tables.

## SQL Analysis

The project includes 12 analytical SQL queries covering:

1. Overall sales performance
2. Sales by company
3. Sales by country
4. Sales by category
5. Sales by fuel type
6. Top 10 best-selling car models
7. Yearly sales analysis
8. Average discount by company
9. Top 10 customers
10. Sales by year, region, company, and model
11. Model performance by category and fuel type
12. Company performance by region

## Python Analysis

Python and Pandas are used to:

- Generate the synthetic dataset
- Connect to SQL Server
- Retrieve data using SQL queries
- Perform data quality checks
- Validate the dataset
- Analyze sales performance
- Create charts and visualizations
- Export analytical results to Excel

The main Python scripts are:

- `generate_data.py`
- `analysis.py`
- `EDA.py`
- `sql_connection.py`

## Excel Report

The Excel report contains analytical results and an interactive dashboard with:

- KPI cards
- Revenue by company
- Revenue by country
- Sales by category
- Sales by fuel type
- Sales trend by year
- Top car models
- Interactive slicers

## Power BI Dashboard

The Power BI dashboard provides an interactive view of global car sales performance.

It includes:

- Total Sales
- Total Cars Sold
- Total Revenue
- Average Sale Price
- Company analysis
- Country analysis
- Region analysis
- Category analysis
- Fuel type analysis
- Top models
- Yearly trends
- Interactive filters and slicers

## Project Structure

```text
Global_Car_Sales_Project/
│
├── DATA/
│   ├── countries.csv
│   ├── companies.csv
│   ├── cars.csv
│   ├── customers.csv
│   └── sales.csv
│
├── PYTHON/
│   ├── generate_data.py
│   ├── analysis.py
│   ├── EDA.py
│   └── sql_connection.py
│
├── SQL/
│   ├── database_setup.sql
│   ├── analysis_queries.sql
│   └── load_data.sql
│
├── EXCEL/
│   └── Global_Car_Sales_Analysis.xlsx
│
├── POWERBI/
│   └── Global_Car_Sales.pbix
│
├── requirements.txt
└── README.md

This project was created for educational purposes. The sales and customer data are synthetic and should not be interpreted as real-world commercial sales data.


Option 1: Run Python analysis directly from CSV files — no SQL Server required.
Option 2: Use SQL Server database for SQL analysi

roject Workflow
Data Generation
      ↓
CSV Files
      ↓
SQL Server Database
      ↓
SQL Analysis
      ↓
Python / Pandas Analysis
      ↓
Excel Report
      ↓
Power BI Dashboard
How to Run the Project
Option 1 — Python Analysis Without SQL Server

The dataset is already available as CSV files inside the DATA folder.

Install the required Python packages:

pip install -r requirements.txt

Then run:

python PYTHON/analysis.py

This option does not require SQL Server.

Option 2 — SQL Server Analysis

If SQL Server Express and SSMS are installed:

Create the GlobalCarSales database using SQL/database_setup.sql.
Load the CSV data using SQL/load_data.sql.
Run the analytical queries from SQL/analysis_queries.sql.
PYTHON/sql_connection.py can then be used to connect Python to SQL Server.

Note: File paths inside load_data.sql may need to be updated if the project is moved to another computer.

Key Insights

The project analyzes:

Sales performance across countries and regions
Company revenue and sales performance
Customer purchasing behavior
Category and fuel-type performance
Best-selling car models
Yearly sales trends
Discount patterns
Revenue distribution
Important Note

This project was created for educational purposes.

The customer and sales data are synthetic and should not be interpreted as real-world commercial sales data.

The car company and model names are used as realistic catalog examples.
