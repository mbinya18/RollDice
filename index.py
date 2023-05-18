import random

def roll_dice():
    """Simulates rolling a dice and returns the result."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print("You rolled:", result)
        play_again = input("Roll again? (y/n): ")
        if play_again.lower() != "y":
            break
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
