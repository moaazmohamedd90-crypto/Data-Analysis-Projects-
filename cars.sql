USE GlobalCarSales;
GO

BULK INSERT Cars
FROM 'C:\Users\HP\OneDrive\Desktop\Global_Car_Sales_Project\cars.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);
GO

SELECT COUNT(*) AS NumberOfCars
FROM Cars;