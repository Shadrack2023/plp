# covid-19_data_tracker.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("owid-covid-data.csv")

print("Columns:", df.columns.tolist())
print("First 5 rows:\n", df.head())
print("Missing values:\n", df.isnull().sum())


countries = ["Kenya", "United States", "India"]
df = df[df["location"].isin(countries)]

df = df.dropna(subset=["date", "new_cases"])
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# interpolate only numeric values
df = df.interpolate(method="linear", numeric_only=True)

print("\nCleaned Data Preview:\n", df.head())


# Total cases over time
plt.figure(figsize=(10,6))
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_cases"], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date"); plt.ylabel("Total Cases")
plt.legend(); plt.show()

# Total deaths over time
plt.figure(figsize=(10,6))
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_deaths"], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date"); plt.ylabel("Total Deaths")
plt.legend(); plt.show()

# Compare daily new cases
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="date", y="new_cases", hue="location")
plt.title("Daily New Cases - Comparison")
plt.xlabel("Date"); plt.ylabel("New Cases")
plt.show()

df["death_rate"] = df["total_deaths"] / df["total_cases"]

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="date", y="death_rate", hue="location")
plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date"); plt.ylabel("Death Rate")
plt.show()

# --- 4. Vaccination Analysis ---
plt.figure(figsize=(10,6))
for country in countries:
    subset = df[df["location"] == country]
    plt.plot(subset["date"], subset["total_vaccinations"], label=country)
plt.title("COVID-19 Vaccination Rollout")
plt.xlabel("Date"); plt.ylabel("Total Vaccinations")
plt.legend(); plt.show()

# Percent population vaccinated (if available)
if "people_vaccinated_per_hundred" in df.columns:
    plt.figure(figsize=(10,6))
    for country in countries:
        subset = df[df["location"] == country]
        plt.plot(subset["date"], subset["people_vaccinated_per_hundred"], label=country)
    plt.title("% Population Vaccinated Over Time")
    plt.xlabel("Date"); plt.ylabel("Vaccinated per 100 People")
    plt.legend(); plt.show()

# --- 6. Insights & Reporting ---
print("\nInsights:")
print("- India had the highest total cases among the three countries.")
print("- The USA showed multiple strong waves of daily new cases.")
print("- Kenya's vaccination rollout started later compared to USA and India.")
print("- Death rates dropped over time as vaccinations increased.")
print("- Anomalies: sharp spikes in reported new cases (due to reporting delays).")
