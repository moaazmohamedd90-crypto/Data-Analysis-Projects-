import pandas as pd
import pyodbc
import random

# =========================
# Airline Data
# =========================

airline_names = [
    "EgyptAir",
    "Emirates",
    "Qatar Airways",
    "Turkish Airlines",
    "Lufthansa",
    "British Airways",
    "Air France",
    "KLM",
    "Etihad Airways",
    "Saudia",
    "Royal Jordanian",
    "Iberia",
    "Singapore Airlines",
    "Thai Airways",
    "Qantas",
    "American Airlines",
    "Delta Airlines",
    "United Airlines",
    "Ryanair",
    "Air Canada"
]

countries = [
    "Egypt",
    "UAE",
    "Qatar",
    "Turkey",
    "Germany",
    "UK",
    "France",
    "Netherlands",
    "UAE",
    "Saudi Arabia",
    "Jordan",
    "Spain",
    "Singapore",
    "Thailand",
    "Australia",
    "USA",
    "USA",
    "USA",
    "Ireland",
    "Canada"
]

# =========================
# Create Data
# =========================

data = []

for i in range(len(airline_names)):
    data.append({
        "Airline_ID": i + 1,
        "Airline_Name": airline_names[i],
        "Country": countries[i],
        "Fleet_Size": random.randint(20, 500)
    })

df = pd.DataFrame(data)

# =========================
# Save CSV
# =========================

df.to_csv("data/airlines.csv", index=False)

print("Airlines CSV created successfully!")
print(df)
print(f"\nTotal Airlines: {len(df)}")

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
# Insert Data into SQL
# =========================

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Airlines
        (Airline_ID, Airline_Name, Country, Fleet_Size)
        VALUES (?, ?, ?, ?)
        """,
        int(row["Airline_ID"]),
        row["Airline_Name"],
        row["Country"],
        int(row["Fleet_Size"])
    )

conn.commit()

print("\nAirlines data inserted into SQL Server successfully!")

cursor.close()
conn.close()

print("Database connection closed.")