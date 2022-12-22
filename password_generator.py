import random
import string

def generate_password(length, characters):
  # Initialize an empty password string
  password = ""

  # Generate the specified number of characters
  for i in range(length):
    # Choose a random character type
    if characters == "letters":
      # Generate a random letter
      char = random.choice(string.ascii_letters)
    elif characters == "numbers":
      # Generate a random digit
      char = random.choice(string.digits)
    elif characters == "special":
      # Generate a random special character
      char = random.choice(string.punctuation)
    elif characters == "all":
      # Generate a random letter, digit, or special character
      char = random.choice(string.ascii_letters + string.digits + string.punctuation)

    # Add the character to the password
    password += char

  # Return the password
  return password

# Get the desired password length and character set from the user
length = int(input("Enter the desired password length: "))
characters = input("Enter the desired character set (letters, numbers, special, all): ")

# Generate and print the password
password = generate_password(length, characters)
print("Generated password:", password)

