from random import randint


print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")
print("Can you guess what it is?")

 # Generate a random number between 1 and 10
secret_number = randint(1, 10)
attempts = 0

while True:
    try:
         guess = int(input("Enter your guess: "))
         attempts += 1

         if guess < secret_number:
            print("Too low! Try again.")
         elif guess > secret_number:
            print("Too high! Try again.")
         else:
             print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
             break
    except ValueError:
        print("Please enter a valid integer.")