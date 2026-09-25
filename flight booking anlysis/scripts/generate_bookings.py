import pandas as pd
import random
import pyodbc
from faker import Faker
from datetime import timedelta

# Initialize Faker
fake = Faker()

# Number of bookings
num_bookings = 5000

# Load existing data
customers = pd.read_csv("data/customers.csv")
flights = pd.read_csv("data/flights.csv")

# Possible values
booking_statuses = [
    "Confirmed",
    "Confirmed",
    "Confirmed",
    "Cancelled",
    "Completed"
]

travel_classes = [
    "Economy",
    "Economy",
    "Economy",
    "Premium Economy",
    "Business",
    "First Class"
]

# Generate booking data
data = []

for i in range(num_bookings):

    # Select customer and flight
    customer_id = random.choice(
        customers["Customer_ID"].tolist()
    )

    flight = flights.sample(1).iloc[0]

    flight_id = int(flight["Flight_ID"])

    # Generate ticket price
    base_price = random.uniform(50, 1000)

    # Travel class multiplier
    travel_class = random.choice(travel_classes)

    if travel_class == "Economy":
        multiplier = 1.0
    elif travel_class == "Premium Economy":
        multiplier = 1.4
    elif travel_class == "Business":
        multiplier = 2.5
    else:
        multiplier = 4.0

    ticket_price = base_price * multiplier
    ticket_price *= random.uniform(0.9, 1.15)

    # Booking date before flight date
    flight_date = pd.to_datetime(
        flight["Departure_Date"]
    )

    booking_date = flight_date - timedelta(
        days=random.randint(1, 180)
    )

    # Make sure booking date is not before 2025
    if booking_date.year < 2025:
        booking_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
            days=random.randint(0, 364)
        )

    # Generate seat number
    seat_number = f"{random.randint(1, 40)}{random.choice(['A', 'B', 'C', 'D', 'E', 'F'])}"

    data.append({
        "Booking_ID": i + 1,
        "Customer_ID": customer_id,
        "Flight_ID": flight_id,
        "Booking_Date": booking_date.date(),
        "Travel_Class": travel_class,
        "Seat_Number": seat_number,
        "Ticket_Price": round(ticket_price, 2),
        "Booking_Status": random.choice(booking_statuses)
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("data/bookings.csv", index=False)

print("Bookings CSV created successfully!")
print(df.head(10))
print(f"\nTotal Bookings: {len(df)}")


# ==============================
# Connect to SQL Server
# ==============================

conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=DESKTOP-NRNK16R\SQLEXPRESS;"
    r"DATABASE=Flight_Booking_Analytics;"
    r"Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Insert data into Bookings
insert_query = """
INSERT INTO Bookings
(
    Booking_ID,
    Customer_ID,
    Flight_ID,
    Booking_Date,
    Travel_Class,
    Seat_Number,
    Ticket_Price,
    Booking_Status
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

for _, row in df.iterrows():

    cursor.execute(
        insert_query,
        int(row["Booking_ID"]),
        int(row["Customer_ID"]),
        int(row["Flight_ID"]),
        row["Booking_Date"],
        row["Travel_Class"],
        row["Seat_Number"],
        float(row["Ticket_Price"]),
        row["Booking_Status"]
    )

conn.commit()

cursor.close()
conn.close()

print("\n5000 bookings inserted into SQL Server successfully!")