USE GlobalCarSales;


-- 1. Overall Sales Analysis
SELECT
    COUNT(*) AS Total_Sales,
    SUM(quantity) AS Total_Cars_Sold,
    SUM(final_price * quantity) AS Total_Revenue,
    AVG(final_price) AS Average_Sale_Price
FROM Sales;


-- 2. Sales by Company
SELECT
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name
ORDER BY Total_Revenue DESC;


-- 3. Sales by Country
SELECT
    co.country_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
GROUP BY co.country_name
ORDER BY Total_Revenue DESC;


-- 4. Sales by Category
SELECT
    ca.category,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.category
ORDER BY Total_Revenue DESC;


-- 5. Sales by Fuel Type
SELECT
    ca.fuel_type,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.fuel_type
ORDER BY Total_Revenue DESC;


-- 6. Top 10 Best-Selling Car Models
SELECT TOP 10
    ca.model,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY ca.model, c.company_name
ORDER BY Total_Sales DESC;


-- 7. Yearly Sales Analysis
SELECT
    YEAR(s.sale_date) AS Sale_Year,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
GROUP BY YEAR(s.sale_date)
ORDER BY Sale_Year;


-- 8. Average Discount by Company
SELECT
    c.company_name,
    AVG(s.discount_percent) AS Average_Discount,
    COUNT(s.sale_id) AS Total_Sales
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name
ORDER BY Average_Discount DESC;


-- 9. Top 10 Customers
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
ORDER BY Total_Spending DESC;


-- 10. Sales by Year, Region, Company and Model
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
    Total_Sales DESC;


-- 11. Model Performance by Category and Fuel Type
SELECT
    c.company_name,
    ca.model,
    ca.category,
    ca.fuel_type,
    COUNT(s.sale_id) AS Total_Sales,
    ROUND(AVG(s.final_price), 2) AS Average_Sale_Price,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY
    c.company_name,
    ca.model,
    ca.category,
    ca.fuel_type
ORDER BY Average_Sale_Price DESC;


-- 12. Company Performance by Region
SELECT
    co.region,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue,
    ROUND(AVG(s.discount_percent), 2) AS Average_Discount
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY
    co.region,
    c.company_name
ORDER BY
    co.region,
    Total_Revenue DESC;


-- same Q BUT WITH MORE detailed information ?

    
SELECT 'Countries' AS TableName, COUNT(*) AS Row_Count FROM Countries
UNION ALL
SELECT 'Companies', COUNT(*) FROM Companies
UNION ALL
SELECT 'Cars', COUNT(*) FROM Cars
UNION ALL
SELECT 'Customers', COUNT(*) FROM Customers
UNION ALL
SELECT 'Sales', COUNT(*) FROM Sales


SELECT
    COUNT(*) AS Total_Sales,
    SUM(quantity) AS Total_Cars_Sold,
    SUM(final_price * quantity) AS Total_Revenue,
    AVG(final_price) AS Average_Sale_Price
FROM Sales;


SELECT
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name
ORDER BY Total_Revenue DESC;

SELECT
    co.country_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
GROUP BY co.country_name
ORDER BY Total_Revenue DESC;

SELECT
    ca.category,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.category
ORDER BY Total_Revenue DESC;

SELECT
    ca.fuel_type,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.fuel_type
ORDER BY Total_Revenue DESC;

SELECT
    ca.model,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY ca.model,c.company_name
ORDER BY Total_Sales DESC;


SELECT
    YEAR(s.sale_date) AS Sale_Year,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
GROUP BY YEAR(s.sale_date)
ORDER BY Sale_Year;


SELECT
    YEAR(s.sale_date) AS Sale_Year,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY YEAR(s.sale_date),c.company_name
ORDER BY Sale_Year,Total_Revenue DESC;

SELECT
    c.company_name,
  ROUND(AVG(s.discount_percent), 2) AS Average_Discount,
    COUNT(s.sale_id) AS Total_Sales
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name
ORDER BY Average_Discount DESC;


SELECT TOP 10
    cu.customer_id,
    cu.customer_name,
    co.country_name,
    COUNT(s.sale_id) AS Total_Purchases,
    SUM(s.final_price * s.quantity) AS Total_Spending
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
GROUP BY cu.customer_id,cu.customer_name,co.country_name
ORDER BY Total_Spending DESC;


SELECT
    co.region,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
GROUP BY co.region
ORDER BY Total_Revenue DESC;

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
GROUP BY YEAR(s.sale_date),co.region,c.company_name,ca.model
ORDER BY Sale_Year,co.region,Total_Sales DESC;


SELECT
    ca.category,
    ca.fuel_type,
    COUNT(s.sale_id) AS Total_Sales,
    ROUND(AVG(s.final_price), 2) AS Average_Sale_Price,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
GROUP BY ca.category,ca.fuel_type
ORDER BY Average_Sale_Price DESC;

SELECT
    c.company_name,
    ca.model,
    ca.category,
    ca.fuel_type,
    COUNT(s.sale_id) AS Total_Sales,
    ROUND(AVG(s.final_price), 2) AS Average_Sale_Price,
    SUM(s.final_price * s.quantity) AS Total_Revenue
FROM Sales s
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY c.company_name,ca.model,ca.category,ca.fuel_type
ORDER BY Average_Sale_Price DESC;


SELECT
    co.region,
    c.company_name,
    COUNT(s.sale_id) AS Total_Sales,
    SUM(s.final_price * s.quantity) AS Total_Revenue,
    ROUND(AVG(s.discount_percent), 2) AS Average_Discount
FROM Sales s
JOIN Customers cu ON s.customer_id = cu.customer_id
JOIN Countries co ON cu.country_id = co.country_id
JOIN Cars ca ON s.car_id = ca.car_id
JOIN Companies c ON ca.company_id = c.company_id
GROUP BY co.region,c.company_name
ORDER BY co.region,Total_Revenue DESC;


