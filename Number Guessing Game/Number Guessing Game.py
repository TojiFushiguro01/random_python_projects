import random

# Function to compare user's guess with the answer
def guess(answer, num):
    # If the guess is correct
    if num == answer:
        return False
    # If the guess is too high
    if num > answer:
        print("Try Again! You guessed TOO HIGH")
        return True
    # If the guess is too low
    if num < answer:
        print("Try Again! You guessed too small")
        return True

# Main game function
def play():
    print("Welcome To The Number Guessing Game!!")
    print("Please Enter a Range to Start -> ")

    try:
        # Get the range bounds from the user
        Lower = int(input("\nEnter the Lower Bound of the Range : "))
        Upper = int(input("Enter the Upper Bound of the Range : "))
    except ValueError:
        print("Enter a Valid Range")
        print("Let's Try Again...")
        play()  # Restart the game if input is invalid

    # Generate a random number within the given range
    Random_number = random.randrange(Lower, Upper)

    print("\nAlright! Now Try Guessing The Number ->")
    
    attempts = 0  # To count number of guesses
    answer = True  # Control variable for the guessing loop

    while answer:
        attempts += 1

        # Offer help if the user has guessed 10 or more times
        if attempts >= 10:
            print("\nLooks like you're having a hard time guessing the number")
            print("Do you need a hint? (-_-)")

            choice = input("\nEnter y or n -> ").lower()

            if choice == 'y':
                print("Let's narrow down your search area")
                mid = (Upper + Lower) // 2  # Find the midpoint of the range
                if mid > Random_number:
                    print("The number is greater than", mid)
                elif mid < Random_number:
                    print("The number is less than", mid)
                else:
                    print("The number is around", mid)
                    
            elif choice == 'n':
                print("That's the spirit, keep going! (*-*)")

        # Get the user's guess
        try:
            num = int(input("\nGuess the Number -> "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is within the range
        if num not in range(Lower, Upper):
            print(f"Error: Input out of range. Enter a number between {Lower} and {Upper}...")
            continue
        
        # Check if the guess is correct
        answer = guess(Random_number, num)

    # If guessed correctly, congratulate the user
    print("\nCongratulations!! You Have Guessed The Number Correctly")
    print(f"Total Number of Guesses = {attempts}")

# Function to ask the user if they want to play the game
def ask():
    ans = input("Enter y or n -> ").lower()

    if ans == 'y':
        play()  # Start the game
    elif ans == 'n':
        print("Are you sure?")
        print("It's a fun game, I think you should give it a try")
        ask()  # Ask again if the user says no
    else:
        print("Please play sincerely\n")
        ask()  # Handle invalid input

# Starting point of the program
print("Wanna play a game?")
ask()
