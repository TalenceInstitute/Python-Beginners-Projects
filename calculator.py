# Define the calculator function
def calculator(num1, num2):
  # Ask the user to choose an operation
  operation = input("Choose an operation (1: addition, 2: subtraction, 3: multiplication, 4: division): ")
  
  # Perform the chosen operation
  if operation == "1":
    # Addition
    result = num1 + num2
  elif operation == "2":
    # Subtraction
    result = num1 - num2
  elif operation == "3":
    # Multiplication
    result = num1 * num2
  elif operation == "4":
    # Division
    result = num1 / num2
  else:
    # Invalid operation
    print("Invalid operation")
    result = None
  return result

# Main program loop
while True:
  # Get the numbers from the user
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  
  # Call the calculator function and print the result
  result = calculator(num1, num2)
  if result is not None:
    print("Result:", result)
  
  # Ask the user if they want to perform another calculation
  again = input("Perform another calculation? (y/n) ")
  if again.lower() != "y":
    break

