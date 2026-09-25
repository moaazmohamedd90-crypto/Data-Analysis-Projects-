# ============================================================
# FLIGHT BOOKING ANALYTICS PROJECT
# Data Cleaning -> EDA -> 25 Business Questions -> Charts
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# ============================================================
# 1) CREATE FOLDERS
# ============================================================

for folder in [
    "analysis",
    "analysis/charts",
    "analysis/interactive_charts",
    "cleaned_data"
]:
    os.makedirs(folder, exist_ok=True)


# ============================================================
# 2) LOAD DATA
# ============================================================

bookings = pd.read_csv("data/bookings.csv")
flights = pd.read_csv("data/flights.csv")
customers = pd.read_csv("data/customers.csv")
airlines = pd.read_csv("data/airlines.csv")
airports = pd.read_csv("data/airports.csv")
passengers = pd.read_csv("data/passengers.csv")


# Keep original sizes
raw_shapes = {
    "Bookings": bookings.shape,
    "Flights": flights.shape,
    "Customers": customers.shape,
    "Airlines": airlines.shape,
    "Airports": airports.shape,
    "Passengers": passengers.shape
}


print("=" * 70)
print("RAW DATA")
print("=" * 70)

for name, shape in raw_shapes.items():
    print(f"{name:<15}: {shape}")


# ============================================================
# 3) STANDARDIZE COLUMN NAMES
# ============================================================

def clean_column_names(df):

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )

    return df


bookings = clean_column_names(bookings)
flights = clean_column_names(flights)
customers = clean_column_names(customers)
airlines = clean_column_names(airlines)
airports = clean_column_names(airports)
passengers = clean_column_names(passengers)


# ============================================================
# 4) CLEAN TEXT COLUMNS
# ============================================================

def clean_text_columns(df):

    df = df.copy()

    for col in df.select_dtypes(include="object").columns:

        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
        )

        df[col] = df[col].replace(
            [
                "",
                "nan",
                "None",
                "NULL",
                "null"
            ],
            pd.NA
        )

    return df


bookings = clean_text_columns(bookings)
flights = clean_text_columns(flights)
customers = clean_text_columns(customers)
airlines = clean_text_columns(airlines)
airports = clean_text_columns(airports)
passengers = clean_text_columns(passengers)


# ============================================================
# 5) STANDARDIZE CATEGORICAL VALUES
# ============================================================

# Bookings
bookings["booking_status"] = (
    bookings["booking_status"]
    .str.strip()
    .str.title()
)

bookings["travel_class"] = (
    bookings["travel_class"]
    .str.strip()
    .str.title()
)


# Flights
flights["flight_status"] = (
    flights["flight_status"]
    .str.strip()
    .str.title()
)


# Customers
customers["gender"] = (
    customers["gender"]
    .str.strip()
    .str.title()
)


# Passengers
passengers["gender"] = (
    passengers["gender"]
    .str.strip()
    .str.title()
)


# ============================================================
# 6) CONVERT DATE COLUMNS
# ============================================================

bookings["booking_date"] = pd.to_datetime(
    bookings["booking_date"],
    errors="coerce"
)

flights["departure_date"] = pd.to_datetime(
    flights["departure_date"],
    errors="coerce"
)

passengers["dateofbirth"] = pd.to_datetime(
    passengers["dateofbirth"],
    errors="coerce"
)


# ============================================================
# 7) CONVERT NUMERIC COLUMNS
# ============================================================

bookings["ticket_price"] = pd.to_numeric(
    bookings["ticket_price"],
    errors="coerce"
)

flights["duration_minutes"] = pd.to_numeric(
    flights["duration_minutes"],
    errors="coerce"
)

customers["age"] = pd.to_numeric(
    customers["age"],
    errors="coerce"
)

airlines["fleet_size"] = pd.to_numeric(
    airlines["fleet_size"],
    errors="coerce"
)


# ============================================================
# 8) CHECK MISSING VALUES
# ============================================================

datasets = {
    "Bookings": bookings,
    "Flights": flights,
    "Customers": customers,
    "Airlines": airlines,
    "Airports": airports,
    "Passengers": passengers
}


print("\n")
print("=" * 70)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 70)

for name, df in datasets.items():

    print(f"\n{name}")

    missing = df.isna().sum()

    print(
        missing[missing > 0]
        if missing.sum() > 0
        else "No missing values"
    )


# ============================================================
# 9) REMOVE EXACT DUPLICATE ROWS
# ============================================================

duplicate_report = {}

for name, df in datasets.items():

    before = len(df)

    df.drop_duplicates(
        inplace=True
    )

    after = len(df)

    duplicate_report[name] = before - after


print("\n")
print("=" * 70)
print("DUPLICATE ROWS REMOVED")
print("=" * 70)

for name, count in duplicate_report.items():

    print(
        f"{name:<15}: {count}"
    )


# ============================================================
# 10) HANDLE MISSING NUMERIC VALUES
# ============================================================

# Ticket price
if bookings["ticket_price"].isna().sum() > 0:

    bookings["ticket_price"] = (
        bookings["ticket_price"]
        .fillna(
            bookings["ticket_price"].median()
        )
    )


# Flight duration
if flights["duration_minutes"].isna().sum() > 0:

    flights["duration_minutes"] = (
        flights["duration_minutes"]
        .fillna(
            flights["duration_minutes"].median()
        )
    )


# Customer age
if customers["age"].isna().sum() > 0:

    customers["age"] = (
        customers["age"]
        .fillna(
            customers["age"].median()
        )
    )


# ============================================================
# 11) REMOVE INVALID VALUES
# ============================================================

# Ticket price cannot be negative
bookings = bookings[
    bookings["ticket_price"] >= 0
].copy()


# Flight duration must be positive
flights = flights[
    flights["duration_minutes"] > 0
].copy()


# Customer age should be between 0 and 100
customers = customers[
    (customers["age"] >= 0) &
    (customers["age"] <= 100)
].copy()


# Fleet size cannot be negative
airlines = airlines[
    airlines["fleet_size"] >= 0
].copy()


# ============================================================
# 12) REMOVE DUPLICATE BUSINESS KEYS
# ============================================================

bookings = bookings.drop_duplicates(
    subset=["booking_id"]
)

flights = flights.drop_duplicates(
    subset=["flight_id"]
)

customers = customers.drop_duplicates(
    subset=["customer_id"]
)

airlines = airlines.drop_duplicates(
    subset=["airline_id"]
)

airports = airports.drop_duplicates(
    subset=["airport_id"]
)

passengers = passengers.drop_duplicates(
    subset=["passengerid"]
)


# ============================================================
# 13) CHECK DATA QUALITY AFTER CLEANING
# ============================================================

print("\n")
print("=" * 70)
print("DATA AFTER CLEANING")
print("=" * 70)

datasets = {
    "Bookings": bookings,
    "Flights": flights,
    "Customers": customers,
    "Airlines": airlines,
    "Airports": airports,
    "Passengers": passengers
}

quality_report = []

for name, df in datasets.items():

    quality_report.append({

        "Dataset": name,

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing_Values":
            int(df.isna().sum().sum()),

        "Duplicate_Rows":
            int(df.duplicated().sum())
    })

    print(
        f"{name:<15}: "
        f"{len(df):,} rows | "
        f"{len(df.columns)} columns"
    )


quality_df = pd.DataFrame(
    quality_report
)

quality_df.to_csv(
    "analysis/data_quality_report.csv",
    index=False
)


# ============================================================
# 14) CHECK RELATIONSHIPS
# ============================================================

valid_flight_ids = set(
    flights["flight_id"].dropna()
)

valid_customer_ids = set(
    customers["customer_id"].dropna()
)

valid_airline_ids = set(
    airlines["airline_id"].dropna()
)

valid_airport_ids = set(
    airports["airport_id"].dropna()
)


orphan_booking_flights = (
    ~bookings["flight_id"]
    .isin(valid_flight_ids)
).sum()


orphan_booking_customers = (
    ~bookings["customer_id"]
    .isin(valid_customer_ids)
).sum()


orphan_flight_airlines = (
    ~flights["airline_id"]
    .isin(valid_airline_ids)
).sum()


orphan_departure_airports = (
    ~flights["departure_airport_id"]
    .isin(valid_airport_ids)
).sum()


orphan_arrival_airports = (
    ~flights["arrival_airport_id"]
    .isin(valid_airport_ids)
).sum()


print("\n")
print("=" * 70)
print("RELATIONSHIP CHECK")
print("=" * 70)

print(
    "Booking -> Flight:",
    orphan_booking_flights
)

print(
    "Booking -> Customer:",
    orphan_booking_customers
)

print(
    "Flight -> Airline:",
    orphan_flight_airlines
)

print(
    "Flight -> Departure Airport:",
    orphan_departure_airports
)

print(
    "Flight -> Arrival Airport:",
    orphan_arrival_airports
)


# ============================================================
# 15) SAVE CLEANED DATA
# ============================================================

bookings.to_csv(
    "cleaned_data/bookings_cleaned.csv",
    index=False
)

flights.to_csv(
    "cleaned_data/flights_cleaned.csv",
    index=False
)

customers.to_csv(
    "cleaned_data/customers_cleaned.csv",
    index=False
)

airlines.to_csv(
    "cleaned_data/airlines_cleaned.csv",
    index=False
)

airports.to_csv(
    "cleaned_data/airports_cleaned.csv",
    index=False
)

passengers.to_csv(
    "cleaned_data/passengers_cleaned.csv",
    index=False
)


# ============================================================
# 16) CREATE ANALYTICAL DATASET
# ============================================================

booking_analysis = bookings.merge(

    flights[
        [
            "flight_id",
            "airline_id",
            "departure_airport_id",
            "arrival_airport_id",
            "departure_date",
            "duration_minutes",
            "flight_status"
        ]
    ],

    on="flight_id",

    how="left"
)


# Add airline
booking_analysis = booking_analysis.merge(

    airlines[
        [
            "airline_id",
            "airline_name",
            "country",
            "fleet_size"
        ]
    ],

    on="airline_id",

    how="left"
)


# Departure airport
departure_airports = airports[
    [
        "airport_id",
        "airport_code",
        "airport_name",
        "city",
        "country"
    ]
].rename(

    columns={

        "airport_id":
            "departure_airport_id",

        "airport_code":
            "departure_code",

        "airport_name":
            "departure_airport_name",

        "city":
            "departure_city",

        "country":
            "departure_country"
    }
)


# Arrival airport
arrival_airports = airports[
    [
        "airport_id",
        "airport_code",
        "airport_name",
        "city",
        "country"
    ]
].rename(

    columns={

        "airport_id":
            "arrival_airport_id",

        "airport_code":
            "arrival_code",

        "airport_name":
            "arrival_airport_name",

        "city":
            "arrival_city",

        "country":
            "arrival_country"
    }
)


booking_analysis = booking_analysis.merge(
    departure_airports,
    on="departure_airport_id",
    how="left"
)


booking_analysis = booking_analysis.merge(
    arrival_airports,
    on="arrival_airport_id",
    how="left"
)


# Create route
booking_analysis["route"] = (

    booking_analysis["departure_code"]
    .fillna("Unknown")

    + " → "

    + booking_analysis["arrival_code"]
    .fillna("Unknown")
)


booking_analysis.to_csv(
    "cleaned_data/booking_analysis.csv",
    index=False
)


# ============================================================
# 17) 25 BUSINESS QUESTIONS
# ============================================================

results = {}


# ------------------------------------------------------------
# Q1 - Total Bookings
# ------------------------------------------------------------

results["Q1_Total_Bookings"] = (
    bookings["booking_id"].nunique()
)


# ------------------------------------------------------------
# Q2 - Total Revenue
# ------------------------------------------------------------

results["Q2_Total_Revenue"] = (
    bookings["ticket_price"].sum()
)


# ------------------------------------------------------------
# Q3 - Average Ticket Price
# ------------------------------------------------------------

results["Q3_Average_Ticket_Price"] = (
    bookings["ticket_price"].mean()
)


# ------------------------------------------------------------
# Q4 - Total Flights
# ------------------------------------------------------------

results["Q4_Total_Flights"] = (
    flights["flight_id"].nunique()
)


# ------------------------------------------------------------
# Q5 - Total Customers
# ------------------------------------------------------------

results["Q5_Total_Customers"] = (
    customers["customer_id"].nunique()
)


# ------------------------------------------------------------
# Q6 - Cancellation Rate
# ------------------------------------------------------------

cancelled_bookings = (
    bookings["booking_status"]
    .eq("Cancelled")
    .sum()
)

total_bookings = len(bookings)

results["Q6_Cancellation_Rate"] = (

    cancelled_bookings /
    total_bookings *
    100
)


# ------------------------------------------------------------
# Q7 - Airline With Most Flights
# ------------------------------------------------------------

q7 = (

    flights

    .merge(
        airlines[
            [
                "airline_id",
                "airline_name"
            ]
        ],

        on="airline_id",

        how="left"
    )

    .groupby(
        "airline_name",
        as_index=False
    )

    .agg(
        Flight_Count=(
            "flight_id",
            "nunique"
        )
    )

    .sort_values(
        "Flight_Count",
        ascending=False
    )
)


results["Q7_Most_Flights_Airline"] = (
    q7.iloc[0]["airline_name"]
)


# ------------------------------------------------------------
# Q8 - Airline With Most Bookings
# ------------------------------------------------------------

q8 = (

    booking_analysis

    .groupby(
        "airline_name",
        as_index=False
    )

    .agg(
        Booking_Count=(
            "booking_id",
            "nunique"
        )
    )

    .sort_values(
        "Booking_Count",
        ascending=False
    )
)


results["Q8_Most_Bookings_Airline"] = (
    q8.iloc[0]["airline_name"]
)


# ------------------------------------------------------------
# Q9 - Airline With Highest Revenue
# ------------------------------------------------------------

q9 = (

    booking_analysis

    .groupby(
        "airline_name",
        as_index=False
    )

    .agg(
        Total_Revenue=(
            "ticket_price",
            "sum"
        )
    )

    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)


results["Q9_Highest_Revenue_Airline"] = (
    q9.iloc[0]["airline_name"]
)


# ------------------------------------------------------------
# Q10 - Highest Average Ticket Price Airline
# ------------------------------------------------------------

q10 = (

    booking_analysis

    .groupby(
        "airline_name",
        as_index=False
    )

    .agg(
        Avg_Ticket_Price=(
            "ticket_price",
            "mean"
        )
    )

    .sort_values(
        "Avg_Ticket_Price",
        ascending=False
    )
)


results["Q10_Highest_Avg_Ticket_Airline"] = (
    q10.iloc[0]["airline_name"]
)


# ------------------------------------------------------------
# Q11 - Longest Average Flight Duration
# ------------------------------------------------------------

q11 = (

    flights

    .merge(
        airlines[
            [
                "airline_id",
                "airline_name"
            ]
        ],

        on="airline_id",

        how="left"
    )

    .groupby(
        "airline_name",
        as_index=False
    )

    .agg(
        Avg_Duration_Minutes=(
            "duration_minutes",
            "mean"
        )
    )

    .sort_values(
        "Avg_Duration_Minutes",
        ascending=False
    )
)


results["Q11_Longest_Avg_Duration_Airline"] = (
    q11.iloc[0]["airline_name"]
)


# ------------------------------------------------------------
# Q12 - Busiest Airport
# ------------------------------------------------------------

departures = (

    flights

    .groupby(
        "departure_airport_id"
    )

    .size()

    .rename("Departures")
)


arrivals = (

    flights

    .groupby(
        "arrival_airport_id"
    )

    .size()

    .rename("Arrivals")
)


q12 = (

    airports

    .merge(
        departures,

        left_on="airport_id",

        right_index=True,

        how="left"
    )

    .merge(
        arrivals,

        left_on="airport_id",

        right_index=True,

        how="left"
    )
)


q12["Departures"] = (
    q12["Departures"]
    .fillna(0)
)


q12["Arrivals"] = (
    q12["Arrivals"]
    .fillna(0)
)


q12["Total_Traffic"] = (

    q12["Departures"] +
    q12["Arrivals"]
)


q12 = q12.sort_values(
    "Total_Traffic",
    ascending=False
)


results["Q12_Busiest_Airport"] = (
    q12.iloc[0]["airport_code"]
)


# ------------------------------------------------------------
# Q13 - Country With Most Airports
# ------------------------------------------------------------

q13 = (

    airports

    .groupby(
        "country",
        as_index=False
    )

    .agg(
        Airport_Count=(
            "airport_id",
            "nunique"
        )
    )

    .sort_values(
        "Airport_Count",
        ascending=False
    )
)


results["Q13_Country_Most_Airports"] = (
    q13.iloc[0]["country"]
)


# ------------------------------------------------------------
# Q14 - Most Active City
# ------------------------------------------------------------

departure_city = (

    flights

    .merge(
        airports[
            [
                "airport_id",
                "city"
            ]
        ],

        left_on="departure_airport_id",

        right_on="airport_id",

        how="left"
    )

    .groupby("city")

    .size()
)


arrival_city = (

    flights

    .merge(
        airports[
            [
                "airport_id",
                "city"
            ]
        ],

        left_on="arrival_airport_id",

        right_on="airport_id",

        how="left"
    )

    .groupby("city")

    .size()
)


q14 = pd.concat(

    [
        departure_city.rename("Departures"),
        arrival_city.rename("Arrivals")
    ],

    axis=1

).fillna(0)


q14["Total_Activity"] = (

    q14["Departures"] +
    q14["Arrivals"]
)


q14 = q14.sort_values(
    "Total_Activity",
    ascending=False
)


results["Q14_Most_Active_City"] = (
    q14.index[0]
)


# ------------------------------------------------------------
# Q15 - Top 10 Busiest Routes
# ------------------------------------------------------------

q15 = (

    booking_analysis

    .groupby(
        "route",
        as_index=False
    )

    .agg(
        Booking_Count=(
            "booking_id",
            "nunique"
        )
    )

    .sort_values(
        "Booking_Count",
        ascending=False
    )

    .head(10)
)


# ------------------------------------------------------------
# Q16 - Route With Highest Bookings
# ------------------------------------------------------------

results["Q16_Highest_Booking_Route"] = (
    q15.iloc[0]["route"]
)


# ------------------------------------------------------------
# Q17 - Route With Highest Revenue
# ------------------------------------------------------------

q17 = (

    booking_analysis

    .groupby(
        "route",
        as_index=False
    )

    .agg(
        Total_Revenue=(
            "ticket_price",
            "sum"
        )
    )

    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)


results["Q17_Highest_Revenue_Route"] = (
    q17.iloc[0]["route"]
)


# ------------------------------------------------------------
# Q18 - Route With Longest Average Duration
# ------------------------------------------------------------

q18 = (

    booking_analysis

    .groupby(
        "route",
        as_index=False
    )

    .agg(
        Avg_Duration_Minutes=(
            "duration_minutes",
            "mean"
        )
    )

    .sort_values(
        "Avg_Duration_Minutes",
        ascending=False
    )
)


results["Q18_Longest_Avg_Duration_Route"] = (
    q18.iloc[0]["route"]
)


# ------------------------------------------------------------
# Q19 - Top 10 Customers By Spending
# ------------------------------------------------------------

q19 = (

    bookings

    .groupby(
        "customer_id",
        as_index=False
    )

    .agg(
        Total_Spending=(
            "ticket_price",
            "sum"
        )
    )

    .sort_values(
        "Total_Spending",
        ascending=False
    )

    .head(10)
)


# ------------------------------------------------------------
# Q20 - Average Spending Per Customer
# ------------------------------------------------------------

customer_spending = (

    bookings

    .groupby(
        "customer_id"
    )

    .agg(
        Total_Spending=(
            "ticket_price",
            "sum"
        )
    )
)


results["Q20_Avg_Spending_Per_Customer"] = (
    customer_spending["Total_Spending"].mean()
)


# ------------------------------------------------------------
# Q21 - Customers Who Never Booked
# ------------------------------------------------------------

booked_customers = set(
    bookings["customer_id"]
    .dropna()
)


never_booked = customers[
    ~customers["customer_id"]
    .isin(booked_customers)
]


results["Q21_Customers_Never_Booked"] = (
    never_booked["customer_id"]
    .nunique()
)


# ------------------------------------------------------------
# Q22 - Customers With More Than One Booking
# ------------------------------------------------------------

booking_frequency = (

    bookings

    .groupby(
        "customer_id"
    )

    .size()
)


results["Q22_Customers_More_Than_One_Booking"] = (

    booking_frequency
    .gt(1)
    .sum()
)


# ------------------------------------------------------------
# Q23 - Travel Class With Highest Revenue
# ------------------------------------------------------------

q23 = (

    bookings

    .groupby(
        "travel_class",
        as_index=False
    )

    .agg(
        Total_Revenue=(
            "ticket_price",
            "sum"
        )
    )

    .sort_values(
        "Total_Revenue",
        ascending=False
    )
)


results["Q23_Highest_Revenue_Travel_Class"] = (
    q23.iloc[0]["travel_class"]
)


# ------------------------------------------------------------
# Q24 - Average Ticket Price By Travel Class
# ------------------------------------------------------------

q24 = (

    bookings

    .groupby(
        "travel_class",
        as_index=False
    )

    .agg(
        Avg_Ticket_Price=(
            "ticket_price",
            "mean"
        )
    )

    .sort_values(
        "Avg_Ticket_Price",
        ascending=False
    )
)


# ------------------------------------------------------------
# Q25 - Monthly Revenue Trend
# ------------------------------------------------------------

monthly_revenue = (

    bookings

    .assign(
        Year_Month=
        bookings["booking_date"]
        .dt.to_period("M")
        .astype(str)
    )

    .groupby(
        "Year_Month",
        as_index=False
    )

    .agg(
        Total_Revenue=(
            "ticket_price",
            "sum"
        )
    )

    .sort_values(
        "Year_Month"
    )
)


# ============================================================
# 18) SAVE QUESTION RESULTS
# ============================================================

q15.to_csv(
    "analysis/q15_top_routes.csv",
    index=False
)

q19.to_csv(
    "analysis/q19_top_customers.csv",
    index=False
)

q23.to_csv(
    "analysis/q23_travel_class_revenue.csv",
    index=False
)

q24.to_csv(
    "analysis/q24_avg_price_by_class.csv",
    index=False
)

monthly_revenue.to_csv(
    "analysis/q25_monthly_revenue.csv",
    index=False
)


# ============================================================
# 19) STATIC CHARTS
# ============================================================

sns.set_theme(
    style="whitegrid"
)


# ------------------------------------------------------------
# Chart 1 - Monthly Revenue
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=monthly_revenue,
    x="Year_Month",
    y="Total_Revenue",
    marker="o"
)

plt.title(
    "Monthly Revenue Trend"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Revenue"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/01_monthly_revenue.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 2 - Bookings By Status
# ------------------------------------------------------------

status_counts = (

    bookings["booking_status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = [
    "Booking_Status",
    "Booking_Count"
]


plt.figure(figsize=(8, 6))

sns.barplot(
    data=status_counts,
    x="Booking_Status",
    y="Booking_Count"
)

plt.title(
    "Bookings by Status"
)

plt.xlabel(
    "Booking Status"
)

plt.ylabel(
    "Bookings"
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/02_bookings_by_status.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 3 - Top 10 Airlines Revenue
# ------------------------------------------------------------

top_airlines = (
    q9
    .head(10)
    .sort_values(
        "Total_Revenue"
    )
)


plt.figure(figsize=(10, 7))

sns.barplot(
    data=top_airlines,
    x="Total_Revenue",
    y="airline_name"
)

plt.title(
    "Top 10 Airlines by Revenue"
)

plt.xlabel(
    "Revenue"
)

plt.ylabel(
    "Airline"
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/03_top_airlines_revenue.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 4 - Average Flight Duration
# ------------------------------------------------------------

top_duration = (
    q11
    .head(10)
    .sort_values(
        "Avg_Duration_Minutes"
    )
)


plt.figure(figsize=(10, 7))

sns.barplot(
    data=top_duration,
    x="Avg_Duration_Minutes",
    y="airline_name"
)

plt.title(
    "Average Flight Duration by Airline"
)

plt.xlabel(
    "Average Duration (Minutes)"
)

plt.ylabel(
    "Airline"
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/04_airline_duration.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 5 - Top Routes
# ------------------------------------------------------------

top_routes = (
    q15
    .sort_values(
        "Booking_Count"
    )
)


plt.figure(figsize=(10, 7))

sns.barplot(
    data=top_routes,
    x="Booking_Count",
    y="route"
)

plt.title(
    "Top 10 Routes by Bookings"
)

plt.xlabel(
    "Bookings"
)

plt.ylabel(
    "Route"
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/05_top_routes.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 6 - Departure Countries
# ------------------------------------------------------------

country_bookings = (

    booking_analysis

    .groupby(
        "departure_country",
        as_index=False
    )

    .agg(
        Booking_Count=(
            "booking_id",
            "nunique"
        )
    )

    .sort_values(
        "Booking_Count",
        ascending=False
    )

    .head(10)

    .sort_values(
        "Booking_Count"
    )
)


plt.figure(figsize=(10, 7))

sns.barplot(
    data=country_bookings,
    x="Booking_Count",
    y="departure_country"
)

plt.title(
    "Top 10 Departure Countries by Bookings"
)

plt.xlabel(
    "Bookings"
)

plt.ylabel(
    "Country"
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/06_departure_country.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 7 - Revenue By Travel Class
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.barplot(
    data=q23,
    x="travel_class",
    y="Total_Revenue"
)

plt.title(
    "Revenue by Travel Class"
)

plt.xlabel(
    "Travel Class"
)

plt.ylabel(
    "Revenue"
)

plt.xticks(
    rotation=20
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/07_travel_class_revenue.png",
    dpi=150
)

plt.close()


# ------------------------------------------------------------
# Chart 8 - Ticket Price Distribution
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    data=bookings,
    x="ticket_price",
    bins=30,
    kde=True
)

plt.title(
    "Ticket Price Distribution"
)

plt.xlabel(
    "Ticket Price"
)

plt.ylabel(
    "Number of Bookings"
)

plt.tight_layout()

plt.savefig(
    "analysis/charts/08_ticket_price_distribution.png",
    dpi=150
)

plt.close()


# ============================================================
# 20) PLOTLY INTERACTIVE CHARTS
# ============================================================


# Interactive Chart 1
fig = px.line(

    monthly_revenue,

    x="Year_Month",

    y="Total_Revenue",

    markers=True,

    title="Monthly Revenue Trend"
)

fig.write_html(
    "analysis/interactive_charts/01_monthly_revenue.html"
)


# Interactive Chart 2
fig = px.bar(

    q9.head(10),

    x="Total_Revenue",

    y="airline_name",

    orientation="h",

    title="Top 10 Airlines by Revenue"
)

fig.write_html(
    "analysis/interactive_charts/02_airlines_revenue.html"
)


# Interactive Chart 3
fig = px.bar(

    q15,

    x="Booking_Count",

    y="route",

    orientation="h",

    title="Top 10 Routes by Bookings"
)

fig.write_html(
    "analysis/interactive_charts/03_top_routes.html"
)


# Interactive Chart 4
fig = px.bar(

    q23,

    x="travel_class",

    y="Total_Revenue",

    title="Revenue by Travel Class"
)

fig.write_html(
    "analysis/interactive_charts/04_travel_class.html"
)


# Interactive Chart 5
fig = px.histogram(

    bookings,

    x="ticket_price",

    nbins=30,

    title="Ticket Price Distribution"
)

fig.write_html(
    "analysis/interactive_charts/05_ticket_price.html"
)


# ============================================================
# 21) SAVE RESULTS
# ============================================================

with open(
    "analysis/python_results.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "FLIGHT BOOKING ANALYTICS RESULTS\n"
    )

    f.write(
        "=" * 60 + "\n\n"
    )

    for key, value in results.items():

        if isinstance(
            value,
            (float, np.floating)
        ):

            if "Rate" in key:

                value = (
                    f"{value:.2f}%"
                )

            else:

                value = (
                    f"{value:,.2f}"
                )

        f.write(
            f"{key}: {value}\n"
        )


# ============================================================
# 22) FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("FLIGHT BOOKING ANALYTICS COMPLETED")
print("=" * 70)

print("\nKEY KPIs")

print(
    f"Total Bookings       : "
    f"{results['Q1_Total_Bookings']:,}"
)

print(
    f"Total Revenue        : "
    f"{results['Q2_Total_Revenue']:,.2f}"
)

print(
    f"Average Ticket Price : "
    f"{results['Q3_Average_Ticket_Price']:,.2f}"
)

print(
    f"Total Flights        : "
    f"{results['Q4_Total_Flights']:,}"
)

print(
    f"Total Customers      : "
    f"{results['Q5_Total_Customers']:,}"
)

print(
    f"Cancellation Rate    : "
    f"{results['Q6_Cancellation_Rate']:.2f}%"
)


print("\nOUTPUTS")

print(
    "Cleaned Data       -> cleaned_data/"
)

print(
    "Static Charts      -> analysis/charts/"
)

print(
    "Interactive Charts -> analysis/interactive_charts/"
)

print(
    "Results            -> analysis/python_results.txt"
)

print(
    "Quality Report     -> analysis/data_quality_report.csv"
)

print("\nDone!")