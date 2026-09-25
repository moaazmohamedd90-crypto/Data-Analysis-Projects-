USE GlobalCarSales;
GO

CREATE TABLE Companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    headquarters_country VARCHAR(100) NOT NULL,
    founded_year INT
);

BULK INSERT Companies
FROM 'C:\Users\HP\OneDrive\Desktop\Global_Car_Sales_Project\companies.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    TABLOCK
);
GO

SELECT COUNT(*) AS Number_Of_Companies
FROM Companies;