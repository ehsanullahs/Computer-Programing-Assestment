# Energy Usage

# Get input values from user
avg_monthly_electric_bill = float(input("\nAverage Monthly Electric bill: "))
avg_monthly_gas_bill = float(input("Average Monthly Gas bill: "))
avg_monthly_fuel_bill = float(input("Average Monthly Fuel bill: "))

constant = 12

# Perform separate calculations
calc1 = avg_monthly_electric_bill * 0.0005 * constant
calc2 = avg_monthly_gas_bill * 0.0053 * constant
calc3 = avg_monthly_fuel_bill * 2.32 * constant

# Final calculations
result = calc1 + calc2 + calc3

# Convert the result to 2 decimal places
rounded_number = round(result, 2)

# Display result
print("Energy Usage is:", rounded_number, "KgCO2", "€")

# Waste

# Get input values from user
avg_monthly_waste = float(input("\nAverage Monthly Waste: "))
avg_monthly_waste_recycled_percentage = float(input("Average Monthly Waste Recycled Percentage: "))

# Perform separate calculations
calc4 = avg_monthly_waste * 12
calc5 = 0.57 - (avg_monthly_waste_recycled_percentage / 100)

# Final calculations
result2 = calc4 * calc5

# Convert the result to 2 decimal places
rounded_number2 = round(result2, 2)

# Display result
print("Waste is:", rounded_number2, "KgCO2", "€")

# Business Travel

# Get input values from user
avg_annual_business_travel_km = float(input("\nAverage Annual Business Travel KM: "))
avg_fuel_efficiency_liters_per_100km = float(input("Average Fuel Efficiency in Liters per 100 KM: "))

# Calculate the amount of CO2 emissions from business travel
business_travel_co2_emissions = (avg_annual_business_travel_km / avg_fuel_efficiency_liters_per_100km) * 2.31

# Convert the result to 2 decimal places
rounded_business_travel_co2_emissions = round(business_travel_co2_emissions, 2)

# Display result
print("Business Travel CO2 Emissions is:", rounded_business_travel_co2_emissions, "KgCO2", "€")