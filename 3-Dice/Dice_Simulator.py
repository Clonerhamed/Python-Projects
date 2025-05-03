import random

def roll_dice(Amount: int):
    
    if Amount <= 0:
        raise ValueError("Amount must be a positive integer.")
    
    rolls = []

    for i in range(Amount):
        random_number = random.randint(1, 6)
        rolls.append(random_number)
        print(f"Roll {i + 1}: {random_number}")

    return rolls

def main():

    while True:
        try:
            Amount = int(input("Enter the number of dice to roll (or 0 to exit): "))
            if Amount == 0:
                print("Exiting the program.")
                break
            rolls = roll_dice(Amount)
            print(f"All rolls: {rolls}")
        except ValueError:
            print("error: Please enter a valid positive integer.")

if __name__ == "__main__":
    main()