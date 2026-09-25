USE GlobalCarSales;
GO

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
SELECT 
    COUNT(*) AS TotalSales,
    COUNT(DISTINCT customer_id) AS UniqueCustomers,
    COUNT(DISTINCT car_id) AS UniqueCars
FROM Sales;
