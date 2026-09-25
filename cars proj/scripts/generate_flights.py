import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import pyodbc

# =========================
# Initialize Faker
# =========================

fake = Faker()

# Number of flights
num_flights = 1000

# =========================
# Load Airlines & Airports
# =========================

airports = pd.read_csv("data/airports.csv")
airlines = pd.read_csv("data/airlines.csv")

airport_ids = airports["Airport_ID"].tolist()
airline_ids = airlines["Airline_ID"].tolist()

# =========================
# Generate Flight Data
# =========================

data = []

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)

flight_statuses = [
    "Scheduled",
    "Completed",
    "Delayed",
    "Cancelled"
]

for i in range(num_flights):

    airline_id = random.choice(airline_ids)

    departure_airport = random.choice(airport_ids)

    arrival_airport = random.choice(airport_ids)

    # Make sure departure and arrival are different
    while arrival_airport == departure_airport:
        arrival_airport = random.choice(airport_ids)

    # Departure date/time
    departure_datetime = fake.date_time_between(
        start_date=start_date,
        end_date=end_date
    )

    # Duration: 1 to 15 hours
    duration_minutes = random.randint(60, 900)

    arrival_datetime = departure_datetime + timedelta(
        minutes=duration_minutes
    )

    data.append({
        "Flight_ID": i + 1,
        "Airline_ID": airline_id,
        "Departure_Airport_ID": departure_airport,
        "Arrival_Airport_ID": arrival_airport,
        "Departure_Date": departure_datetime.date(),
        "Departure_Time": departure_datetime.time(),
        "Arrival_Time": arrival_datetime.time(),
        "Duration_Minutes": duration_minutes,
        "Flight_Status": random.choice(flight_statuses)
    })

# =========================
# Create DataFrame
# =========================

df = pd.DataFrame(data)

# =========================
# Save CSV
# =========================

df.to_csv("data/flights.csv", index=False)

print("Flights CSV created successfully!")
print(df.head(10))
print(f"\nTotal Flights: {len(df)}")

# =========================
# Connect to SQL Server
# =========================

conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=DESKTOP-NRNK16R\SQLEXPRESS;"
    r"DATABASE=Flight_Booking_Analytics;"
    r"Trusted_Connection=yes;"
)

cursor = conn.cursor()

# =========================
# Insert Flights
# =========================

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Flights
        (
            Flight_ID,
            Airline_ID,
            Departure_Airport_ID,
            Arrival_Airport_ID,
            Departure_Date,
            Departure_Time,
            Arrival_Time,
            Duration_Minutes,
            Flight_Status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        int(row["Flight_ID"]),
        int(row["Airline_ID"]),
        int(row["Departure_Airport_ID"]),
        int(row["Arrival_Airport_ID"]),
        row["Departure_Date"],
        row["Departure_Time"],
        row["Arrival_Time"],
        int(row["Duration_Minutes"]),
        row["Flight_Status"]
    )

conn.commit()

print("\nFlights data inserted into SQL Server successfully!")

cursor.close()
conn.close()

print("Database connection closed.")