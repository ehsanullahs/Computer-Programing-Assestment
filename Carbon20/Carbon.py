def carbon_footprint(activity, quantity):
  """Calculates the carbon footprint of an activity.

  Args:
    activity: The activity, e.g. "driving", "flying", or "heating".
    quantity: The quantity of the activity, e.g. 100 miles, 1 flight, or 1000 kWh.

  Returns:
    The carbon footprint of the activity in pounds CO2e.
  """

  carbon_footprints = {
    "driving": 40,
    "flying": 200,
    "heating": 100,
  }

  return carbon_footprints[activity] * quantity


if __name__ == "__main__":
  print(carbon_footprint("driving", 100))  # 4000 pounds CO2e
  print(carbon_footprint("flying", 1))  # 200 pounds CO2e
  print(carbon_footprint("heating", 1000))  # 10000 pounds CO2e