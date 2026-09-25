USE GlobalCarSales;
GO

BULK INSERT Customers
FROM 'C:\Users\HP\OneDrive\Desktop\Global_Car_Sales_Project\customers.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);
GO

SELECT COUNT(*) AS NumberOfCustomers
FROM Customers;