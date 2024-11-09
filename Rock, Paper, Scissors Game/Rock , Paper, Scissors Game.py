import random

def play():
    # Display choices for the user
    print("Choose: 'r' for Rock, 'p' for Paper, 's' for Scissors")
    
    # Define possible moves
    move = ['r', 'p', 's']
    
    # Randomly choose a move for the computer
    computer = random.choice(move)
    
    # Get the user's choice and convert to lowercase
    user = input("Enter your choice: ").lower()

    # Show user and computer choices
    print(f"User choice : {user}")
    print(f"Computer choice : {computer}")
    
    # Check if the user made a valid choice
    if user not in move:
        print("Invalid Choice")
        return  # Exit the function if the choice is invalid

    # Check for a draw
    if computer == user:
        print("It's a Draw")
        return  # Exit the function if it's a draw

    # Rock, Paper, Scissors game logic
    if user == 'r':
        if computer == 'p':
            print("You Lose!")  # Rock loses to Paper
        elif computer == 's':
            print("You Win!")   # Rock beats Scissors
    elif user == 'p':
        if computer == 's':
            print("You Lose!")  # Paper loses to Scissors
        elif computer == 'r':
            print("You Win!")   # Paper beats Rock
    elif user == 's':
        if computer == 'r':
            print("You Lose!")  # Scissors lose to Rock
        elif computer == 'p':
            print("You Win!")   # Scissors beat Paper
            
# Ask the user if they want to play the game
choose = input("Wanna Play rock, paper, scissors [Y/n]: \n ").lower()

# Loop to keep playing the game until the user says 'n'
while choose == 'y':
    play()  # Call the play function
    choose = input("Play Again [Y/n]: \n ").lower()  # Ask to play again
    
    if choose == 'n':
        print("Bye bye!!")
        break  # Exit the loop if the user doesn't want to play again
