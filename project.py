# --- SETUP ---
import pandas as pd
import matplotlib.pyplot as plt
import requests
from scipy.stats import ttest_ind

# READ CITIBIKE TRIP DATA 
bike_df = pd.read_csv("citibike_merged.csv")
bike_df["started_at"] = pd.to_datetime(bike_df["started_at"])
bike_df["date"] = bike_df["started_at"].dt.date

# FETCH WEATHER DATA (Jan+Feb 2025) 
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 40.71,
    "longitude": -74.01,
    "start_date": "2025-01-01",
    "end_date": "2025-02-28",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/New_York"
}

response = requests.get(url, params=params)
print("Status Code:", response.status_code)
weather_json = response.json()

if "daily" in weather_json:
    weather_df = pd.DataFrame(weather_json["daily"])
    weather_df.rename(columns={"time": "date"}, inplace=True)
    weather_df["date"] = pd.to_datetime(weather_df["date"]).dt.date
    weather_df["rainy"] = weather_df["precipitation_sum"] > 1.0
else:
    print("❌ Failed to retrieve daily weather data.")
    weather_df = None

#ANALYSIS 
if weather_df is not None:
    # Count rides per day
    daily_trips = bike_df.groupby("date").size().reset_index(name="trip_count")

    # Merge trips and weather
    merged = pd.merge(weather_df, daily_trips, on="date", how="left")
    merged["trip_count"] = merged["trip_count"].fillna(0).astype(int)

    # Add weekend info
    merged["weekend"] = pd.to_datetime(merged["date"]).dt.weekday >= 5  # Saturday=5, Sunday=6

    #PLOTTING 

    ## (1) Daily Total Trips (Rainy Days Highlighted)
    plt.figure(figsize=(14,6))
    colors = ["red" if r else "steelblue" for r in merged["rainy"]]
    plt.bar(merged["date"], merged["trip_count"], color=colors)
    plt.title("Daily Total Bike Rides - Jan + Feb 2025 (Red = Rainy Day)")
    plt.xlabel("Date")
    plt.ylabel("Number of Bike Rides")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("daily_trip_counts.png")
    plt.show()

    ## (2) Boxplot: Dry vs Rainy Days
    plt.figure(figsize=(8,6))
    data_rain = [merged[~merged["rainy"]]["trip_count"], merged[merged["rainy"]]["trip_count"]]
    plt.boxplot(data_rain, labels=["Dry Days", "Rainy Days"])
    plt.title("Bike Rides Distribution - Dry vs Rainy Days")
    plt.ylabel("Number of Bike Rides")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("boxplot_rainy_vs_dry.png")
    plt.show()

    ## (3) Boxplot: Weekday vs Weekend
    plt.figure(figsize=(8,6))
    data_weekend = [merged[~merged["weekend"]]["trip_count"], merged[merged["weekend"]]["trip_count"]]
    plt.boxplot(data_weekend, labels=["Weekday", "Weekend"])
    plt.title("Bike Rides Distribution - Weekday vs Weekend")
    plt.ylabel("Number of Bike Rides")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("boxplot_weekday_vs_weekend.png")
    plt.show()

    #HYPOTHESIS TESTING 

    ## (a) Rainy Days vs Dry Days
    rainy = merged[merged["rainy"]]["trip_count"]
    non_rainy = merged[~merged["rainy"]]["trip_count"]

    t_stat_rain, p_val_rain = ttest_ind(rainy, non_rainy, equal_var=False)

    print(f"\nT-Statistic (Rain Effect): {t_stat_rain:.2f}")
    print(f"P-Value (Rain Effect): {p_val_rain:.4f}")
    if p_val_rain < 0.05:
        print(" Statistically significant difference: Rain impacts bike rentals.")
    else:
        print(" No significant difference: Rain does not significantly affect rentals.")

    ## (b) Weekend vs Weekday
    weekend_days = merged[merged["weekend"]]["trip_count"]
    weekday_days = merged[~merged["weekend"]]["trip_count"]

    t_stat_weekend, p_val_weekend = ttest_ind(weekend_days, weekday_days, equal_var=False)

    print(f"\nT-Statistic (Weekend Effect): {t_stat_weekend:.2f}")
    print(f"P-Value (Weekend Effect): {p_val_weekend:.4f}")
    if p_val_weekend < 0.05:
        print(" Statistically significant difference: Weekends impact bike rentals.")
    else:
        print(" No significant difference: Weekends do not significantly affect rentals.")

else:
    print(" Skipping analysis because weather data could not be retrieved.")
