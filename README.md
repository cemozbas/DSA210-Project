# Bike Rental Demand Analysis: Trends & Influencing Factors


# Project Overview
 Whether you’re a tourist or a local, renting bikes can be a great activity for individuals and families alike. This project examines the extent to which various factors influence bike rental demand, including weather conditions, temperature, holidays, and other external events. By analyzing these variables, the study aims to quantify their impact and identify which factors play the most significant role in shaping rental trends.

# Dataset

This project uses data from two primary sources:

1. Citi Bike System Data 

The main dataset comes from Citi Bike, a bike-sharing service in New York City. It includes:
	•	Date & Time – Timestamp of each rental.
	•	Start & End Station – Location of rental pickup and drop-off.
	•	Trip Duration – Total ride time in minutes.
	•	User Type – Subscriber vs. casual rider.

📌 Source: [ Citi Bike System Data](https://ride.citibikenyc.com/system-data)

2. Open-Meteo Historical Weather API 

To analyze the impact of weather on bike rental demand, historical weather data is obtained from Open-Meteo’s Historical Weather API. The dataset includes:
	•	Temperature (°C) – Outdoor temperature at 2m height.
	•	Precipitation (mm) – Total rainfall per hour.
	•	Cloud Cover (%) – Low, mid, and high cloud coverage.
	•	Wind Speed (m/s) – Wind speed at 10m height.

📌 Source: [ Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)

# Research Questions
• How much does temperature affect bike rental demand? 

• Do rainy or windy conditions significantly decrease ridership? 

• Are holidays associated with increased or decreased bike rentals? 

• What are the peak times and days for bike rentals?


# Hypothesis


Null Hypothesis (H₀):

Weather conditions, holidays, and time of day have no significant impact on bike rental demand.

Alternative Hypothesis (H₁):

External factors significantly influence bike rental demand, with measurable effects:
		
  •Higher temperatures increase ridership up to an optimal range, beyond which extreme heat reduces rentals.
		
  •Rain and strong winds lead to a decline in rentals.
		
  •Holidays and major events cause noticeable increase in demand.

# Methods
 1. Data Collection – Retrieve Citi Bike trip records and Open-Meteo weather data.
 2.  Data Cleaning – Handle missing values, format timestamps, and merge datasets.  
 3.  Exploratory Data Analysis (EDA) – Identify trends and visualize rental patterns.  
 4.  Statistical Analysis – Perform correlation tests and regression modeling to assess the impact of weather and holidays.


# Limitations and Future Work
Limitations:
		
  •Data is limited to New York City, making results location-dependent.
		
  •Other external factors (e.g., traffic, bike availability) are not included.

Future Improvements:
		
  •Expand analysis to other cities for comparison.
		
  •Use real-time data for predictive modeling.
