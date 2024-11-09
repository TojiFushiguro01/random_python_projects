def play():
    # Initialize the score to zero
    score = 0

    # First question
    ans1 = input("What game studio makes the Red Dead Redemption series? = ")
    if ans1.lower() == "rockstar games":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Second question
    ans2 = input("What planet is closest to the sun? = ")
    if ans2.lower() == "mercury":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Third question
    ans3 = input("Where is the strongest human muscle located? = ")
    if ans3.lower() == "jaw":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Fourth question
    ans4 = input("Who was the first Disney princess? = ")
    if ans4.lower() == "snow white":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Fifth question
    ans5 = input("How many Dragon Balls are there? = ")
    if ans5.lower() == "seven":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Display the final score
    print(f"You have answered {score} Questions Correctly!!")
    print("\n\nThank you For Playing!! ^-^")

# Start of the quiz game
print("Welcome to My Quiz game!")

# Ask the user if they want to play
reply = input("Do you want to play [Y/n] - ").lower()

# If user refuses, keep asking until they agree
while reply == "n":
    print("Huh... just play it once, will you!\n")
    reply = input("Do you want to play [Y/n] - ").lower()

# Start the game if the user agrees
if reply == "y":
    print("\nAlright! Here we go~")
    play()
