import random
import sys

class RPS: 
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.score = {"player": 0, "computer": 0}
        self.current_round = 1
    def play(self):
       
        while True:
            player_choice = input(f"Round {self.current_round} - Enter rock, paper, or scissors (or 'q' to quit): ").lower()
            if player_choice == 'q':
                print("Thanks for playing!")
                sys.exit()
            if player_choice not in self.options:
                print("Invalid choice. Please try again.")
                continue

            computer_choice = random.choice(self.options)
            print(f"Computer chose: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("You win!")
                self.score["player"] += 1

            else:
                print("You lose!")
                self.score["computer"] += 1
            
            if self.score["player"] == 3:
                print("Congratulations! You won the game!")
                break
            elif self.score["computer"] == 3:
                print("Sorry! The computer won the game.")
                break

            print(f"Score - Player: {self.score['player']}, Computer: {self.score['computer']}")
            self.current_round += 1
        print("Game over! Thanks for playing.")
        print(f"Final Score - Player: {self.score['player']}, Computer: {self.score['computer']}")

if __name__ == "__main__":
    game = RPS()
    game.play()

