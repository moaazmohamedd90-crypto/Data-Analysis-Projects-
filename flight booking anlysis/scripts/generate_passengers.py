import pandas as pd
from faker import Faker
import random
import pyodbc

# =========================
# Initialize Faker
# =========================

fake = Faker()

# Number of customers
num_customers = 500

# Possible values
genders = ["Male", "Female"]

countries = [
    "Egypt",
    "Saudi Arabia",
    "UAE",
    "Qatar",
    "Jordan",
    "Turkey",
    "UK",
    "Germany",
    "France",
    "USA",
    "Canada",
    "Australia",
    "Spain",
    "Italy",
    "India"
]

# =========================
# Generate Customer Data
# =========================

data = []

for i in range(num_customers):

    data.append({
        "Customer_ID": i + 1,
        "First_Name": fake.first_name(),
        "Last_Name": fake.last_name(),
        "Gender": random.choice(genders),
        "Age": random.randint(18, 70),
        "Country": random.choice(countries)
    })

# =========================
# Create DataFrame
# =========================

df = pd.DataFrame(data)

# =========================
# Save CSV
# =========================

df.to_csv("data/customers.csv", index=False)

print("Customers CSV created successfully!")
print(df.head(10))
print(f"\nTotal Customers: {len(df)}")

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
# Insert Customers
# =========================

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Customers
        (Customer_ID, First_Name, Last_Name, Gender, Age, Country)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        int(row["Customer_ID"]),
        row["First_Name"],
        row["Last_Name"],
        row["Gender"],
        int(row["Age"]),
        row["Country"]
    )

conn.commit()

print("\nCustomers data inserted into SQL Server successfully!")

cursor.close()
conn.close()

print("Database connection closed.")
