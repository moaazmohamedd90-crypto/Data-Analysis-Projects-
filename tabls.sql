CREATE DATABASE GlobalCarSales;
GO
USE GlobalCarSales;
GO
CREATE TABLE Countries (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL
);
GO

CREATE TABLE Companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    headquarters_country VARCHAR(100) NOT NULL,
    founded_year INT
);
GO
CREATE TABLE Cars (
    car_id INT PRIMARY KEY,
    company_id INT NOT NULL,
    model VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    fuel_type VARCHAR(50) NOT NULL,
    model_year INT,
    price DECIMAL(12,2),

    CONSTRAINT FK_Cars_Companies
        FOREIGN KEY (company_id)
        REFERENCES Companies(company_id)
);
GO
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    gender VARCHAR(20),
    age INT,
    country_id INT NOT NULL,
    email VARCHAR(150),
    phone VARCHAR(50),
    registration_date DATE,

    CONSTRAINT FK_Customers_Countries
        FOREIGN KEY (country_id)
        REFERENCES Countries(country_id)
);
GO
USE GlobalCarSales;
GO

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    car_id INT NOT NULL,
    sale_date DATE NOT NULL,
    quantity INT NOT NULL,
    discount_percent DECIMAL(5,2),
    final_price DECIMAL(12,2) NOT NULL,

    CONSTRAINT FK_Sales_Customers
        FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id),

    CONSTRAINT FK_Sales_Cars
        FOREIGN KEY (car_id)
        REFERENCES Cars(car_id)
);
GO

USE GlobalCarSales;
GO
