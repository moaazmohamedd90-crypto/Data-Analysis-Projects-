import pandas as pd
import pyodbc

# =========================
# Airport Data
# =========================

airports = [
    [1, "CAI", "Cairo International Airport", "Cairo", "Egypt"],
    [2, "HBE", "Borg El Arab International Airport", "Alexandria", "Egypt"],
    [3, "DXB", "Dubai International Airport", "Dubai", "UAE"],
    [4, "AUH", "Zayed International Airport", "Abu Dhabi", "UAE"],
    [5, "DOH", "Hamad International Airport", "Doha", "Qatar"],
    [6, "IST", "Istanbul Airport", "Istanbul", "Turkey"],
    [7, "LHR", "Heathrow Airport", "London", "UK"],
    [8, "CDG", "Charles de Gaulle Airport", "Paris", "France"],
    [9, "FRA", "Frankfurt Airport", "Frankfurt", "Germany"],
    [10, "AMS", "Amsterdam Airport Schiphol", "Amsterdam", "Netherlands"],
    [11, "JFK", "John F. Kennedy International Airport", "New York", "USA"],
    [12, "LAX", "Los Angeles International Airport", "Los Angeles", "USA"],
    [13, "ORD", "O'Hare International Airport", "Chicago", "USA"],
    [14, "YYZ", "Toronto Pearson International Airport", "Toronto", "Canada"],
    [15, "SIN", "Singapore Changi Airport", "Singapore", "Singapore"],
    [16, "BKK", "Suvarnabhumi Airport", "Bangkok", "Thailand"],
    [17, "SYD", "Sydney Kingsford Smith Airport", "Sydney", "Australia"],
    [18, "MAD", "Adolfo Suarez Madrid-Barajas Airport", "Madrid", "Spain"],
    [19, "RUH", "King Khalid International Airport", "Riyadh", "Saudi Arabia"],
    [20, "AMM", "Queen Alia International Airport", "Amman", "Jordan"]
]

# =========================
# Create DataFrame
# =========================

columns = [
    "Airport_ID",
    "Airport_Code",
    "Airport_Name",
    "City",
    "Country"
]

df = pd.DataFrame(airports, columns=columns)

# =========================
# Save CSV
# =========================

df.to_csv("data/airports.csv", index=False)

print("Airports CSV created successfully!")
print(df)
print(f"\nTotal Airports: {len(df)}")

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
# Insert into SQL Server
# =========================

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Airports
        (Airport_ID, Airport_Code, Airport_Name, City, Country)
        VALUES (?, ?, ?, ?, ?)
        """,
        int(row["Airport_ID"]),
        row["Airport_Code"],
        row["Airport_Name"],
        row["City"],
        row["Country"]
    )

conn.commit()

print("\nAirports data inserted into SQL Server successfully!")

cursor.close()
conn.close()

print("Database connection closed.")