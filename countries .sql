USE GlobalCarSales;
GO

BULK INSERT Countries
FROM 'C:\Users\HP\OneDrive\Desktop\Global_Car_Sales_Project\sales.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);
GO

SELECT COUNT(*) AS NumberOfSales
FROM Countries;
GO