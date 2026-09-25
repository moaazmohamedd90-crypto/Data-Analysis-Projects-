-- 1. What is the total number of bookings?
SELECT COUNT(*) AS Total_Bookings
FROM Bookings;


-- 2. What is the total revenue?
SELECT SUM(Ticket_Price) AS Total_Revenue
FROM Bookings;


-- 3. What is the average ticket price?
SELECT AVG(Ticket_Price) AS Average_Ticket_Price
FROM Bookings;


-- 4. What is the booking cancellation rate?
SELECT
    COUNT(CASE WHEN Booking_Status = 'Cancelled' THEN 1 END) * 100.0
    / COUNT(*) AS Cancellation_Rate
FROM Bookings;


-- 5. Which airline generates the highest revenue?
SELECT TOP 1
    a.Airline_Name,
    SUM(b.Ticket_Price) AS Total_Revenue
FROM Airlines a
JOIN Flights f
    ON a.Airline_ID = f.Airline_ID
JOIN Bookings b
    ON f.Flight_ID = b.Flight_ID
GROUP BY a.Airline_Name
ORDER BY Total_Revenue DESC;


-- 6. Which airline receives the most bookings?
SELECT TOP 1
    a.Airline_Name,
    COUNT(b.Booking_ID) AS Total_Bookings
FROM Airlines a
JOIN Flights f
    ON a.Airline_ID = f.Airline_ID
JOIN Bookings b
    ON f.Flight_ID = b.Flight_ID
GROUP BY a.Airline_Name
ORDER BY Total_Bookings DESC;


-- 7. Which airline has the longest average flight duration?
SELECT TOP 1
    a.Airline_Name,
    AVG(f.Duration_Minutes) AS Average_Duration
FROM Airlines a
JOIN Flights f
    ON a.Airline_ID = f.Airline_ID
GROUP BY a.Airline_Name
ORDER BY Average_Duration DESC;


-- 8. Which route has the highest number of bookings?
SELECT TOP 1
    d.City AS Departure_City,
    ar.City AS Arrival_City,
    COUNT(b.Booking_ID) AS Total_Bookings
FROM Flights f
JOIN Airports d
    ON f.Departure_Airport_ID = d.Airport_ID
JOIN Airports ar
    ON f.Arrival_Airport_ID = ar.Airport_ID
JOIN Bookings b
    ON f.Flight_ID = b.Flight_ID
GROUP BY d.City, ar.City
ORDER BY Total_Bookings DESC;


-- 9. What are the top 10 busiest routes?
SELECT TOP 10
    d.City AS Departure_City,
    ar.City AS Arrival_City,
    COUNT(f.Flight_ID) AS Total_Flights
FROM Flights f
JOIN Airports d
    ON f.Departure_Airport_ID = d.Airport_ID
JOIN Airports ar
    ON f.Arrival_Airport_ID = ar.Airport_ID
GROUP BY d.City, ar.City
ORDER BY Total_Flights DESC;


-- 10. Which countries have the most airports?
SELECT
    Country,
    COUNT(*) AS Total_Airports
FROM Airports
GROUP BY Country
ORDER BY Total_Airports DESC;


-- 11. What is the distribution of bookings by status?
SELECT
    Booking_Status,
    COUNT(*) AS Total_Bookings
FROM Bookings
GROUP BY Booking_Status
ORDER BY Total_Bookings DESC;


-- 12. Which travel class generates the highest revenue?
SELECT TOP 1
    Travel_Class,
    SUM(Ticket_Price) AS Total_Revenue
FROM Bookings
GROUP BY Travel_Class
ORDER BY Total_Revenue DESC;


-- 13. What is the monthly revenue trend?
SELECT
    YEAR(Booking_Date) AS Booking_Year,
    MONTH(Booking_Date) AS Booking_Month,
    SUM(Ticket_Price) AS Total_Revenue
FROM Bookings
GROUP BY
    YEAR(Booking_Date),
    MONTH(Booking_Date)
ORDER BY
    Booking_Year,
    Booking_Month;


-- 14. What is the distribution of flights by status?
SELECT
    Flight_Status,
    COUNT(*) AS Total_Flights
FROM Flights
GROUP BY Flight_Status
ORDER BY Total_Flights DESC;


-- 15. What is the average flight duration?
SELECT
    AVG(Duration_Minutes) AS Average_Flight_Duration
FROM Flights;