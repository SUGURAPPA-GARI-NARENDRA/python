def celsius_to_fahrenheit(celsius):
  """Converts temperature from Celsius to Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
  """Converts temperature from Fahrenheit to Celsius."""
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# Get user input for the temperature and the scale
try:
  temp_value = float(input("Enter the temperature value: "))
  scale = input("Enter the scale (C for Celsius or F for Fahrenheit): ").upper()

  if scale == 'C':
    converted_temp = celsius_to_fahrenheit(temp_value)
    print(f"{temp_value}°C is equal to {converted_temp:.2f}°F")
  elif scale == 'F':
    converted_temp = fahrenheit_to_celsius(temp_value)
    print(f"{temp_value}°F is equal to {converted_temp:.2f}°C")
  else:
    print("Invalid scale. Please enter 'C' or 'F'.")

except ValueError:
  print("Invalid input. Please enter a valid number for the temperature.")

