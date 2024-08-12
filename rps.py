from enum import Enum
import random

class Choice(Enum):
    ROCK: int = 1
    PAPER: int = 2
    SCISSORS: int = 3

def main():
    print("Options: rock, paper, scissors")
    choice = input("Choose an option: ")

    if choice not in {'rock', 'paper', 'scissors'}:
        print(f"Invalid choice: {choice}")
        return

    choice = Choice[choice.upper()]

    # 1-3 was too repetitive, so this will make it more random.
    random_number = random.randint(1, 30)
    response = Choice((random_number - 1) // 10 + 1)

    if choice == response:
        print("Tie! Try again.")
        main()
    elif (choice == Choice.ROCK and response == Choice.SCISSORS) or \
         (choice == Choice.PAPER and response == Choice.ROCK) or \
         (choice == Choice.SCISSORS and response == Choice.PAPER):
        print("You won!")
    else:
        print("You lost!")

    exit(0)

if __name__ == "__main__":
    main()
