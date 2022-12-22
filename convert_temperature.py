def convert_temperature(temp):
  # Check if the temperature is in Celsius or Fahrenheit
  if temp.endswith("C"):
    # Convert Celsius to Fahrenheit
    temp_f = (9/5) * float(temp[:-1]) + 32
    return "{:.1f}F".format(temp_f)
  elif temp.endswith("F"):
    # Convert Fahrenheit to Celsius
    temp_c = (5/9) * (float(temp[:-1]) - 32)
    return "{:.1f}C".format(temp_c)

# Get the temperature and scale from the user
temp = input("Enter a temperature and scale (e.g. 32C or 75F): ")

# Convert and print the temperature
converted_temp = convert_temperature(temp)
print("Converted temperature:", converted_temp)

