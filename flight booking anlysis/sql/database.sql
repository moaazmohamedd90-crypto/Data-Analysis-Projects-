-- =============================================
-- Flight Booking Analytics
-- Database Creation Script
-- =============================================

-- Create Database
CREATE DATABASE FlightBookingAnalytics;
GO

-- Use Database
USE FlightBookingAnalytics;
GO


-- =============================================
-- 1. Airlines Table
-- =============================================

CREATE TABLE Airlines (
    AirlineID INT PRIMARY KEY,
    AirlineName VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    AirlineType VARCHAR(50) NOT NULL,
    FoundedYear INT,
    Website VARCHAR(255)
);
GO


-- =============================================
-- 2. Airports Table
-- =============================================

CREATE TABLE Airports (
    AirportID INT PRIMARY KEY,
    AirportCode CHAR(3) NOT NULL UNIQUE,
    AirportName VARCHAR(150) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Continent VARCHAR(50) NOT NULL,
    AirportType VARCHAR(50) NOT NULL
);
GO


-- =============================================
-- 3. Passengers Table
-- =============================================

CREATE TABLE Passengers (
    PassengerID INT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Nationality VARCHAR(100) NOT NULL,
    Email VARCHAR(150) NOT NULL UNIQUE,
    Phone VARCHAR(50),
    PassportNumber VARCHAR(20) NOT NULL UNIQUE
);
GO


-- =============================================
-- 4. Flights Table
-- =============================================

CREATE TABLE Flights (
    FlightID INT PRIMARY KEY,
    FlightNumber VARCHAR(20) NOT NULL,
    
    AirlineID INT NOT NULL,
    
    DepartureAirportID INT NOT NULL,
    ArrivalAirportID INT NOT NULL,
    
    DepartureDate DATETIME NOT NULL,
    ArrivalDate DATETIME NOT NULL,
    
    DurationHours INT NOT NULL,
    AvailableSeats INT NOT NULL,
    BasePrice DECIMAL(10,2) NOT NULL,

    -- Airline Relationship
    CONSTRAINT FK_Flights_Airlines
        FOREIGN KEY (AirlineID)
        REFERENCES Airlines(AirlineID),

    -- Departure Airport Relationship
    CONSTRAINT FK_Flights_DepartureAirport
        FOREIGN KEY (DepartureAirportID)
        REFERENCES Airports(AirportID),

    -- Arrival Airport Relationship
    CONSTRAINT FK_Flights_ArrivalAirport
        FOREIGN KEY (ArrivalAirportID)
        REFERENCES Airports(AirportID)
);
GO


-- =============================================
-- 5. Bookings Table
-- =============================================

CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY,

    PassengerID INT NOT NULL,
    FlightID INT NOT NULL,

    BookingDate DATETIME NOT NULL,
    SeatClass VARCHAR(50) NOT NULL,
    TicketPrice DECIMAL(10,2) NOT NULL,
    BookingStatus VARCHAR(50) NOT NULL,
    PaymentMethod VARCHAR(50) NOT NULL,

    -- Passenger Relationship
    CONSTRAINT FK_Bookings_Passengers
        FOREIGN KEY (PassengerID)
        REFERENCES Passengers(PassengerID),

    -- Flight Relationship
    CONSTRAINT FK_Bookings_Flights
        FOREIGN KEY (FlightID)
        REFERENCES Flights(FlightID)
);
GO


-- =============================================
-- Database Structure Completed
-- =============================================

PRINT 'FlightBookingAnalytics Database Created Successfully!';
GO