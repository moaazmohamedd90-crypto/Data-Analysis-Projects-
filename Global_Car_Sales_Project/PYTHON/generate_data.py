import pandas as pd
from faker import Faker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "DATA"
companies = [
    # === القائمة الأصلية (30 شركة) ===
    ("Toyota", "Japan", 1937),
    ("BMW", "Germany", 1916),
    ("Ford", "USA", 1903),
    ("Mercedes-Benz", "Germany", 1926),
    ("Hyundai", "South Korea", 1967),
    ("Kia", "South Korea", 1944),
    ("Honda", "Japan", 1948),
    ("Audi", "Germany", 1909),
    ("Volkswagen", "Germany", 1937),
    ("Nissan", "Japan", 1933),
    ("Chevrolet", "USA", 1911),
    ("Tesla", "USA", 2003),
    ("Volvo", "Sweden", 1927),
    ("Porsche", "Germany", 1931),
    ("Lexus", "Japan", 1989),

    ("Alfa Romeo", "Italy", 1910),
    ("Aston Martin", "United Kingdom", 1913),
    ("Bentley", "United Kingdom", 1919),
    ("Bugatti", "France", 1909),
    ("Buick", "USA", 1899),
    ("BYD Auto", "China", 2003),
    ("Cadillac", "USA", 1902),
    ("Chery", "China", 1997),
    ("Chrysler", "USA", 1925),
    ("Citroën", "France", 1919),
    ("Dacia", "Romania", 1966),
    ("Daewoo Motors", "South Korea", 1937),
    ("Daihatsu", "Japan", 1951),
    ("Dodge", "USA", 1900),
    ("Ferrari", "Italy", 1939),
    ("Fiat", "Italy", 1899),
    ("Geely", "China", 1986),
    ("Genesis Motor", "South Korea", 2015),
    ("Great Wall Motors", "China", 1984),
    ("Jaguar", "United Kingdom", 1935),
    ("Koenigsegg", "Sweden", 1994),
    ("Lamborghini", "Italy", 1963),
    ("Land Rover", "United Kingdom", 1948),
    ("Lincoln", "USA", 1917),
    ("Maserati", "Italy", 1914),
    ("Mazda", "Japan", 1920),
    ("McLaren", "United Kingdom", 1985),
    ("Mitsubishi", "Japan", 1970),
    ("Peugeot", "France", 1896),
    ("Renault", "France", 1899)
]

company_data = []

for i, company in enumerate(companies, start=1):
    company_data.append({
        "company_id": i,
        "company_name": company[0],
        "headquarters_country": company[1],
        "founded_year": company[2]
    })

companies_df = pd.DataFrame(company_data)

print(companies_df)

companies_df.to_csv(DATA_DIR / "companies.csv", index=False)

# -----------------------------
# Countries Table
# -----------------------------

countries = [
    # === القائمة الأصلية (20 دولة) ===
    ("Egypt", "Africa"),
    ("USA", "North America"),
    ("Canada", "North America"),
    ("Germany", "Europe"),
    ("France", "Europe"),
    ("United Kingdom", "Europe"),
    ("Italy", "Europe"),
    ("Spain", "Europe"),
    ("Japan", "Asia"),
    ("South Korea", "Asia"),
    ("China", "Asia"),
    ("India", "Asia"),
    ("Australia", "Oceania"),
    ("Brazil", "South America"),
    ("Mexico", "North America"),
    ("United Arab Emirates", "Asia"),
    ("Saudi Arabia", "Asia"),
    ("South Africa", "Africa"),
    ("Sweden", "Europe"),
    ("Netherlands", "Europe"),

    ("Algeria", "Africa"),
    ("Nigeria", "Africa"),
    ("Kenya", "Africa"),
    ("Morocco", "Africa"),
    ("Ghana", "Africa"),
    ("Argentina", "South America"),
    ("Chile", "South America"),
    ("Peru", "South America"),
    ("Colombia", "South America"),
    ("Venezuela", "South America"),
    ("Turkey", "Asia"),         
    ("Pakistan", "Asia"),
    ("Bangladesh", "Asia"),
    ("Indonesia", "Asia"),
    ("Malaysia", "Asia"),
    ("Singapore", "Asia"),
    ("Thailand", "Asia"),
    ("Vietnam", "Asia"),
    ("Philippines", "Asia"),
    ("Israel", "Asia"),
    ("Kuwait", "Asia"),
    ("Qatar", "Asia"),
    ("Oman", "Asia"),
    ("Switzerland", "Europe"),
    ("Belgium", "Europe"),
    ("Portugal", "Europe"),
    ("Greece", "Europe"),
    ("Austria", "Europe"),
    ("Norway", "Europe"),
    ("Denmark", "Europe"),
    ("Finland", "Europe"),
    ("Poland", "Europe"),
    ("Ireland", "Europe"),
    ("New Zealand", "Oceania")
]

country_data = []

for i, country in enumerate(countries, start=1):
    country_data.append({
        "country_id": i,
        "country_name": country[0],
        "region": country[1]
    })

countries_df = pd.DataFrame(country_data)

print("\nCountries Table:")
print(countries_df)
countries_df.to_csv(DATA_DIR / "countries.csv", index=False)

# -----------------------------
# Cars Table
# -----------------------------

car_models = {

    # Toyota
    1: [
        ("Corolla", "Sedan", "Petrol", 24000),
        ("Camry", "Sedan", "Hybrid", 32000),
        ("RAV4", "SUV", "Hybrid", 38000),
        ("Land Cruiser", "SUV", "Petrol", 85000)
    ],

    # BMW
    2: [
        ("3 Series", "Sedan", "Petrol", 48000),
        ("5 Series", "Sedan", "Hybrid", 62000),
        ("X3", "SUV", "Petrol", 55000),
        ("X5", "SUV", "Hybrid", 75000)
    ],

    # Ford
    3: [
        ("Focus", "Hatchback", "Petrol", 23000),
        ("Mustang", "Sports", "Petrol", 45000),
        ("Explorer", "SUV", "Petrol", 48000),
        ("F-150", "Pickup", "Petrol", 50000)
    ],

    # Mercedes-Benz
    4: [
        ("A-Class", "Sedan", "Petrol", 42000),
        ("C-Class", "Sedan", "Hybrid", 55000),
        ("GLC", "SUV", "Hybrid", 65000),
        ("GLE", "SUV", "Petrol", 85000)
    ],

    # Hyundai
    5: [
        ("Elantra", "Sedan", "Petrol", 22000),
        ("Sonata", "Sedan", "Hybrid", 28000),
        ("Tucson", "SUV", "Hybrid", 33000),
        ("Ioniq 5", "Electric", "Electric", 45000)
    ],

    # Kia
    6: [
        ("Cerato", "Sedan", "Petrol", 23000),
        ("Sportage", "SUV", "Hybrid", 32000),
        ("Sorento", "SUV", "Hybrid", 40000),
        ("EV6", "Electric", "Electric", 48000)
    ],

    # Honda
    7: [
        ("Civic", "Sedan", "Petrol", 25000),
        ("Accord", "Sedan", "Hybrid", 32000),
        ("CR-V", "SUV", "Hybrid", 36000),
        ("Pilot", "SUV", "Petrol", 48000)
    ],

    # Audi
    8: [
        ("A3", "Sedan", "Petrol", 39000),
        ("A4", "Sedan", "Hybrid", 48000),
        ("Q5", "SUV", "Hybrid", 58000),
        ("Q8", "SUV", "Petrol", 78000)
    ],

    # Volkswagen
    9: [
        ("Golf", "Hatchback", "Petrol", 26000),
        ("Passat", "Sedan", "Petrol", 32000),
        ("Tiguan", "SUV", "Petrol", 35000),
        ("ID.4", "Electric", "Electric", 42000)
    ],

    # Nissan
    10: [
        ("Sunny", "Sedan", "Petrol", 19000),
        ("Altima", "Sedan", "Petrol", 28000),
        ("X-Trail", "SUV", "Hybrid", 35000),
        ("Leaf", "Electric", "Electric", 30000)
    ],

    # Chevrolet
    11: [
        ("Malibu", "Sedan", "Petrol", 25000),
        ("Camaro", "Sports", "Petrol", 40000),
        ("Tahoe", "SUV", "Petrol", 60000),
        ("Silverado", "Pickup", "Petrol", 50000)
    ],

    # Tesla
    12: [
        ("Model 3", "Sedan", "Electric", 42000),
        ("Model Y", "SUV", "Electric", 48000),
        ("Model S", "Sedan", "Electric", 80000),
        ("Model X", "SUV", "Electric", 90000)
    ],

    # Volvo
    13: [
        ("S60", "Sedan", "Hybrid", 45000),
        ("S90", "Sedan", "Hybrid", 58000),
        ("XC40", "SUV", "Electric", 48000),
        ("XC90", "SUV", "Hybrid", 70000)
    ],

    # Porsche
    14: [
        ("718 Cayman", "Sports", "Petrol", 65000),
        ("911", "Sports", "Petrol", 120000),
        ("Macan", "SUV", "Petrol", 65000),
        ("Taycan", "Electric", "Electric", 95000)
    ],

    # Lexus
    15: [
        ("IS", "Sedan", "Hybrid", 42000),
        ("ES", "Sedan", "Hybrid", 48000),
        ("NX", "SUV", "Hybrid", 50000),
        ("LX", "SUV", "Petrol", 90000)
    ],

    # Alfa Romeo
    16: [
        ("Giulia", "Sedan", "Petrol", 45000),
        ("Stelvio", "SUV", "Petrol", 52000),
        ("Tonale", "SUV", "Hybrid", 38000)
    ],

    # Aston Martin
    17: [
        ("Vantage", "Sports", "Petrol", 150000),
        ("DB12", "Sports", "Petrol", 220000),
        ("DBX", "SUV", "Petrol", 190000)
    ],

    # Bentley
    18: [
        ("Continental GT", "Sports", "Petrol", 250000),
        ("Flying Spur", "Sedan", "Petrol", 230000),
        ("Bentayga", "SUV", "Hybrid", 200000)
    ],

    # Bugatti
    19: [
        ("Chiron", "Sports", "Petrol", 3000000),
        ("Mistral", "Sports", "Petrol", 5000000)
    ],

    # Buick
    20: [
        ("Encore", "SUV", "Petrol", 28000),
        ("Envision", "SUV", "Petrol", 35000),
        ("Enclave", "SUV", "Petrol", 45000)
    ],

    # BYD Auto
    21: [
        ("Dolphin", "Hatchback", "Electric", 22000),
        ("Seal", "Sedan", "Electric", 40000),
        ("Atto 3", "SUV", "Electric", 35000)
    ],

    # Cadillac
    22: [
        ("CT4", "Sedan", "Petrol", 38000),
        ("Escalade", "SUV", "Petrol", 85000),
        ("Lyriq", "SUV", "Electric", 60000)
    ],

    # Chery
    23: [
        ("Tiggo 4", "SUV", "Petrol", 22000),
        ("Tiggo 7", "SUV", "Petrol", 28000),
        ("Tiggo 8", "SUV", "Hybrid", 35000)
    ],

    # Chrysler
    24: [
        ("300", "Sedan", "Petrol", 35000),
        ("Pacifica", "Van", "Hybrid", 48000)
    ],

    # Citroën
    25: [
        ("C3", "Hatchback", "Petrol", 20000),
        ("C4", "Hatchback", "Electric", 28000),
        ("C5 Aircross", "SUV", "Hybrid", 35000)
    ],

    # Dacia
    26: [
        ("Sandero", "Hatchback", "Petrol", 15000),
        ("Duster", "SUV", "Petrol", 22000),
        ("Jogger", "SUV", "Hybrid", 26000)
    ],

    # Daewoo Motors
    27: [
        ("Lanos", "Sedan", "Petrol", 18000),
        ("Matiz", "Hatchback", "Petrol", 14000)
    ],

    # Daihatsu
    28: [
        ("Terios", "SUV", "Petrol", 20000),
        ("Mira", "Hatchback", "Petrol", 15000),
        ("Rocky", "SUV", "Petrol", 22000)
    ],

    # Dodge
    29: [
        ("Charger", "Sedan", "Petrol", 45000),
        ("Challenger", "Sports", "Petrol", 50000),
        ("Durango", "SUV", "Petrol", 55000)
    ],

    # Ferrari
    30: [
        ("Roma", "Sports", "Petrol", 250000),
        ("296 GTB", "Sports", "Hybrid", 350000),
        ("SF90", "Sports", "Hybrid", 500000)
    ],

    # Fiat
    31: [
        ("500", "Hatchback", "Petrol", 18000),
        ("Tipo", "Sedan", "Petrol", 22000),
        ("500e", "Electric", "Electric", 30000)
    ],

    # Geely
    32: [
        ("Emgrand", "Sedan", "Petrol", 20000),
        ("Coolray", "SUV", "Petrol", 25000),
        ("Geometry C", "Electric", "Electric", 30000)
    ],

    # Genesis
    33: [
        ("G70", "Sedan", "Petrol", 45000),
        ("G80", "Sedan", "Hybrid", 60000),
        ("GV70", "SUV", "Hybrid", 55000)
    ],

    # Great Wall Motors
    34: [
        ("Haval Jolion", "SUV", "Petrol", 22000),
        ("Haval H6", "SUV", "Hybrid", 30000),
        ("Poer", "Pickup", "Petrol", 28000)
    ],

    # Jaguar
    35: [
        ("XE", "Sedan", "Petrol", 45000),
        ("F-Pace", "SUV", "Petrol", 60000),
        ("F-Type", "Sports", "Petrol", 75000)
    ],

    # Koenigsegg
    36: [
        ("Jesko", "Sports", "Petrol", 3000000),
        ("Regera", "Sports", "Hybrid", 2000000)
    ],

    # Lamborghini
    37: [
        ("Huracan", "Sports", "Petrol", 250000),
        ("Urus", "SUV", "Petrol", 230000),
        ("Revuelto", "Sports", "Hybrid", 600000)
    ],

    # Land Rover
    38: [
        ("Defender", "SUV", "Petrol", 60000),
        ("Discovery", "SUV", "Hybrid", 70000),
        ("Range Rover", "SUV", "Hybrid", 110000)
    ],

    # Lincoln
    39: [
        ("Corsair", "SUV", "Hybrid", 40000),
        ("Nautilus", "SUV", "Hybrid", 55000),
        ("Navigator", "SUV", "Petrol", 80000)
    ],

    # Maserati
    40: [
        ("Ghibli", "Sedan", "Petrol", 85000),
        ("Levante", "SUV", "Petrol", 95000),
        ("GranTurismo", "Sports", "Petrol", 150000)
    ],

    # Mazda
    41: [
        ("Mazda 3", "Sedan", "Petrol", 24000),
        ("CX-5", "SUV", "Petrol", 30000),
        ("CX-60", "SUV", "Hybrid", 45000)
    ],

    # McLaren
    42: [
        ("Artura", "Sports", "Hybrid", 250000),
        ("720S", "Sports", "Petrol", 300000)
    ],

    # Mitsubishi
    43: [
        ("Lancer", "Sedan", "Petrol", 22000),
        ("Outlander", "SUV", "Hybrid", 35000),
        ("Eclipse Cross", "SUV", "Hybrid", 30000)
    ],

    # Peugeot
    44: [
        ("208", "Hatchback", "Petrol", 21000),
        ("308", "Hatchback", "Hybrid", 28000),
        ("3008", "SUV", "Hybrid", 38000)
    ],

    # Renault
    45: [
        ("Clio", "Hatchback", "Petrol", 20000),
        ("Megane", "Hatchback", "Hybrid", 28000),
        ("Austral", "SUV", "Hybrid", 35000)
    ]
}


car_data = []

car_id = 1

for company_id, models in car_models.items():

    for model in models:

        car_data.append({
            "car_id": car_id,
            "company_id": company_id,
            "model": model[0],
            "category": model[1],
            "fuel_type": model[2],
            "model_year": 2025,
            "price": model[3]
        })

        car_id += 1


cars_df = pd.DataFrame(car_data)

print("\nCars Table:")
print(cars_df)

cars_df.to_csv(DATA_DIR / "cars.csv", index=False)

# -----------------------------
# Customers Table
# -----------------------------
import random

fake = Faker()

customers_data = []

for i in range(1, 2001):

    country_id = random.randint(1, len(countries_df))

    customers_data.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 65),
        "country_id": country_id,
        "email": fake.email(),
        "phone": fake.phone_number(),
        "registration_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })


customers_df = pd.DataFrame(customers_data)

print("\nCustomers Table:")
print(customers_df.head())

print("\nNumber of Customers:", len(customers_df))

customers_df.to_csv(DATA_DIR / "customers.csv", index=False)
# -----------------------------
# Sales Table
# -----------------------------

sales_data = []

for i in range(1, 10001):

    customer_id = random.randint(1, len(customers_df))
    car_id = random.randint(1, len(cars_df))

    sale_date = fake.date_between(
        start_date="-3y",
        end_date="today"
    )

    quantity = 1

    # Get car price
    car_price = cars_df.loc[
        cars_df["car_id"] == car_id,
        "price"
    ].iloc[0]

    # Generate discount between 0% and 15%
    discount_percent = random.randint(0, 15)

    discount_amount = car_price * discount_percent / 100

    final_price = car_price - discount_amount

    sales_data.append({
        "sale_id": i,
        "customer_id": customer_id,
        "car_id": car_id,
        "sale_date": sale_date,
        "quantity": quantity,
        "discount_percent": discount_percent,
        "final_price": round(final_price, 2)
    })


sales_df = pd.DataFrame(sales_data)

print("\nSales Table:")
print(sales_df.head())

print("\nNumber of Sales:", len(sales_df))

sales_df.to_csv(DATA_DIR / "sales.csv", index=False)