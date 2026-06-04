# Exercise 8 – Weight Converter
# Converts weight between kilograms, pounds, grams, and ounces.

weight_init = float(input("Enter the weight: "))
measurement_init = input("Enter kg/lb or g/oz: ")
print()

if measurement_init == "g":
    grams = weight_init
    kilograms = grams / 1000
    ounces = grams / 28.3495231
    pounds = grams / 453.59237
elif measurement_init == "kg":
    kilograms = weight_init
    grams = kilograms * 1000
    ounces = kilograms * 35.273962
    pounds = kilograms * 2.20462262
elif measurement_init == "oz":
    ounces = weight_init
    grams = ounces * 28.3495231
    kilograms = ounces / 35.273962
    pounds = ounces / 16
elif measurement_init == "lb":
    pounds = weight_init
    grams = pounds * 453.59237
    kilograms = pounds / 2.20462262
    ounces = pounds * 16
else:
    print("Please enter a valid input.")
    exit(0)

print(f"The weight is {grams:.4f} g")
print(f"The weight is {kilograms:.4f} kg")
print(f"The weight is {ounces:.4f} oz")
print(f"The weight is {pounds:.4f} lb")

# TODO:
# - [easy] Make input case-insensitive so “KG”, “Kg”, or “LBS” still work.
# - [medium] Add a loop allowing multiple conversions in one run.
# - [hard] Expand into a full unit converter with categories like distance, temperature, and volume.

# UPDATE LOG:
# 1.1.0 (2025-10-07) [feature] [medium] – Completed TODO: Added support for grams and ounces in addition to kg and lbs.
# 1.0.0 (N/A) [init] – Initial working version (basic kg ↔ lbs converter).

