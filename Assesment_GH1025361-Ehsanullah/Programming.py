def calculate_energy_usage():
  """Calculates the total energy usage based on the given electric bill, gas bill, and fuel bill.

  Args:
    electric_bill: The average monthly electric bill.
    gas_bill: The average monthly gas bill.
    fuel_bill: The average monthly fuel bill.

  Returns:
    The total energy usage in kWh.
  """

  # Get input values from the user with validation
  average_monthly_electricity_bill_in_euros = float(input("What is your average monthly electricity bill in euros? "))
  while average_monthly_electricity_bill_in_euros <= 0:
    print("Invalid input. Please enter a positive number.")
    average_monthly_electricity_bill_in_euros = float(input("What is your average monthly electricity bill in euros? "))

  electric_bill = average_monthly_electricity_bill_in_euros * 0.9005
  gas_bill = float(input("Enter your average monthly gas bill: "))
  while gas_bill <= 0:
    print("Invalid input. Please enter a positive number.")
    gas_bill = float(input("Enter your average monthly gas bill: "))

  fuel_bill = float(input("Enter your average monthly fuel bill: "))
  while fuel_bill <= 0:
    print("Invalid input. Please enter a positive number.")
    fuel_bill = float(input("Enter your average monthly fuel bill: "))

  # Get average monthly natural gas bill in euros
  average_monthly_natural_gas_bill_in_euros = gas_bill / 0.9e53

  # Get average monthly fuel bill for transportation in euros
  average_monthly_fuel_bill_for_transportation_in_euros = fuel_bill / 2.32

  # Perform separate calculations
  electric_bill_calc = electric_bill
  gas_bill_calc = gas_bill_calc
  fuel_bill_calc = fuel_bill_calc

  # Final calculation
  result = electric_bill_calc + gas_bill_calc + fuel_bill_calc

  return round(result, 2)

if __name__ == "__main__":
  total_energy_usage = calculate_energy_usage()
  print(f"Your total energy usage is {total_energy_usage} kWh.")
