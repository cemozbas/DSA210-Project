# Bike Rental Demand Analysis: Impact of Weather and Weekends

## Project Overview

This project investigates how **weather conditions** and **day type** (weekend vs weekday) influence the **bike rental demand** in New York City.  
By integrating trip records from Citi Bike and historical weather data from Open-Meteo, we perform an exploratory and statistical analysis to identify how external factors affect the number of daily rides.

This study aims to:
- Measure the impact of rainy weather on bike usage
- Analyze behavioral patterns between weekdays and weekends
- Quantify statistical significance of observed trends

## Datasets

### 1. Citi Bike System Data

The primary dataset comes from **Citi Bike**, New York City's bike-sharing service.  
It includes detailed ride-level information:

- **Start Date & Time**: When the trip began
- **End Date & Time**: When the trip ended
- **Start & End Stations**: Location IDs
- **User Type**: Subscriber vs casual user
- **Trip Duration**

📌 Source: [Citi Bike System Data](https://ride.citibikenyc.com/system-data)

---

### 2. Open-Meteo Historical Weather API

Historical weather conditions were retrieved from **Open-Meteo**'s archive API.  
The daily weather information contains:

- **Date**
- **Max and Min Temperatures** (°C)
- **Precipitation Sum** (mm)
- **Rainy Day Label** (>1mm rainfall considered "rainy")

📌 Source: [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)

---

## Data Collection Period

- **From:** January 1, 2025
- **To:** February 28, 2025
- **Duration:** 60 days
- **Location:** New York City, USA

---

## Research Questions

- Do rainy days significantly reduce daily bike ride numbers?
- Is there a meaningful difference between weekday and weekend bike usage?
- How do daily trip counts fluctuate over time during the winter months?

---

## Hypotheses

### 1. Rain Impact Hypothesis

- **Null Hypothesis (H₀):** Rainy days have no significant effect on bike rentals.
- **Alternative Hypothesis (H₁):** Rainy days significantly decrease bike rentals.

### 2. Weekend Impact Hypothesis

- **Null Hypothesis (H₀):** Weekends have no significant effect on bike rental numbers.
- **Alternative Hypothesis (H₁):** Weekends significantly influence bike rental numbers compared to weekdays.

---

## Methods

1. **Data Cleaning and Preparation**
   - Parsed timestamps and extracted dates
   - Merged bike rental data with daily weather conditions
   - Labeled days as rainy or dry, and weekend or weekday

2. **Exploratory Data Analysis (EDA)**
   - Plotted total daily bike trips
   - Highlighted rainy days in time series
   - Compared trip distributions across rain and weekend categories using boxplots

3. **Statistical Hypothesis Testing**
   - **Independent two-sample t-tests** to compare:
     - Rainy days vs dry days
     - Weekends vs weekdays
   - Calculated p-values and interpreted significance at α = 0.05

---

## 📈 Visualizations

- **Daily Trip Counts** (rainy days highlighted in red)
- **Boxplot: Dry Days vs Rainy Days**
- **Boxplot: Weekdays vs Weekends**

> All plots are saved as `.png` files in the repository for easy viewing.

---

## Results Summary

### 1. Rain Effect

- **T-statistic**: (calculated in script)
- **P-value**: (calculated in script)

**Interpretation:**  
If p < 0.05 → Rainy days significantly reduce bike rentals.  
Otherwise → No significant difference detected.

---

### 2. Weekend Effect

- **T-statistic**: (calculated in script)
- **P-value**: (calculated in script)

**Interpretation:**  
If p < 0.05 → Weekend bike rental patterns are significantly different from weekdays.  
Otherwise → No significant difference detected.

---

## Limitations and Future Work

**Limitations:**
- Study only covers January and February (winter months).
- NYC bike behavior may vary greatly in spring/summer seasons.
- No breakdown by user type (e.g., subscriber vs casual).

**Future Work:**
- Extend study to a full calendar year for seasonal trends.
- Analyze user types separately (commuters vs tourists).
- Predict bike rental demand using machine learning models.

---

# 🚲 Special Notes

- Rain was considered significant if daily precipitation > **1.0 mm**.
- A **weekend** was defined as Saturday or Sunday.
- Data for holidays was excluded from analysis due to insufficient sample size.

---
