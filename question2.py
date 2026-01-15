import math

# Dictionaries to store data
season_temp = {
    "Summer": [],
    "Autumn": [],
    "Winter": [],
    "Spring": []
}

station_temp = {}

# Ask user for number of records
while True:
    try:
        n = int(input("Enter total number of temperature records: "))
        if n <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Input temperature records from user
for i in range(n):
    print(f"\nRecord {i + 1}:")

    # Get valid date
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        parts = date.split("-")
        if len(parts) != 3:
            print("Invalid date format! Use YYYY-MM-DD.")
            continue
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            if month < 1 or month > 12 or day < 1 or day > 31:
                print("Invalid month/day. Please enter valid numbers.")
                continue
            break
        except ValueError:
            print("Date must contain numbers only.")

    # Get station name
    station = input("Enter station name: ").strip()
    if station == "":
        print("Station name empty. Skipping record.")
        continue

    # Get temperature
    temp_input = input("Enter temperature (or leave blank if missing): ").strip()
    if temp_input == "" or temp_input.lower() == "nan":
        print("Temperature missing. Skipping record.")
        continue
    try:
        temp = float(temp_input)
    except ValueError:
        print("Invalid temperature. Skipping record.")
        continue

    # Determine Australian season
    if month in [12, 1, 2]:
        season = "Summer"
    elif month in [3, 4, 5]:
        season = "Autumn"
    elif month in [6, 7, 8]:
        season = "Winter"
    else:
        season = "Spring"

    # Add to seasonal data
    season_temp[season].append(temp)

    # Add to station data
    if station not in station_temp:
        station_temp[station] = []
    station_temp[station].append(temp)

# -------------------------------------------------
# 1. Seasonal Average
# -------------------------------------------------
print("\n--- Seasonal Average Temperature ---")
for s in ["Summer", "Autumn", "Winter", "Spring"]:
    if len(season_temp[s]) > 0:
        avg = sum(season_temp[s]) / len(season_temp[s])
        print(f"{s}: {avg:.1f}°C")
    else:
        print(f"{s}: No data")

# -------------------------------------------------
# 2. Largest Temperature Range
# -------------------------------------------------
max_range = 0
ranges = {}

for st, temps in station_temp.items():
    if len(temps) == 0:
        continue
    r = max(temps) - min(temps)
    ranges[st] = r
    if r > max_range:
        max_range = r

print("\n--- Station(s) with Largest Temperature Range ---")
for st, r in ranges.items():
    if r == max_range:
        print(f"Station {st}: Range {r:.1f}°C "
              f"(Max: {max(station_temp[st]):.1f}°C, Min: {min(station_temp[st]):.1f}°C)")

# -------------------------------------------------
# 3. Temperature Stability (Standard Deviation)
# -------------------------------------------------
std_values = {}
for st, temps in station_temp.items():
    if len(temps) == 0:
        continue
    mean = sum(temps) / len(temps)
    variance = sum((t - mean) ** 2 for t in temps) / len(temps)
    std = math.sqrt(variance)
    std_values[st] = std

if len(std_values) == 0:
    print("\nNo temperature data available for stability analysis.")
else:
    min_std = min(std_values.values())
    max_std = max(std_values.values())

    print("\n--- Temperature Stability ---")
    for st, std in std_values.items():
        if std == min_std:
            print(f"Most Stable : Station {st}: StdDev {std:.1f}°C")
    for st, std in std_values.items():
        if std == max_std:
            print(f"Most Variable : Station {st}: StdDev {std:.1f}°C")
