# Exercise 9 – Temperature Conversion
# Converts temperature between Celsius and Fahrenheit.

temperature = float(input("Enter temperature: "))
unit = input("Enter c/f: ")

if unit.upper() == "C":
    temperature_1 = (temperature * 1.8) + 32
    unit_1 = "F"
elif unit.upper() == "F":
    temperature_1 = (temperature - 32) / 1.8
    unit_1 = "C"
else:
    print("Invalid unit")

print(f"{temperature}°{unit} is {round(temperature_1,1)}°{unit_1}")

# TODO:
# - [easy] Format the output to include a clearer sentence (e.g., “The temperature in Fahrenheit is…”).
# - [medium] Allow conversions between Kelvin, Celsius, and Fahrenheit.
# - [hard] Build a temperature conversion menu with explanations of each formula.

# UPDATE LOG:
# 1.1.0 (2025-10-10) [feature] [easy] – Completed TODO: Made input case-insensitive so “c”, “C”, “f”, or “F” all work.
# 1.0.0 (N/A) [init] – Initial working version (C ↔ F converter).
