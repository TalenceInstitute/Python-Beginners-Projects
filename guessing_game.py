import random

def guessing_game(max_number):
  # Specify the maximum number of attempts
  max_attempts = 5

  # Generate a random number between 1 and max_number
  secret_number = random.randint(1, max_number)

  # Initialize the number of attempts
  attempts = 0

  # Start the guessing loop
  while True:
    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if guess == secret_number:
      print("You win! You guessed the correct number in", attempts, "attempts.")
      break
    elif guess < secret_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")

    # Check if the user has run out of attempts
    if attempts >= max_attempts:
      print("You lose! The correct number was", secret_number)
      break

# Main program
def main():
    # Specify the maximum number for the secret number
    max_number = 100
    guessing_game(max_number)
    
  
# Run the main program
if __name__ == "__main__": 
    main()
