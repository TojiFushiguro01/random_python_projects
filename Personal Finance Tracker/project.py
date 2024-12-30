import csv
import sys
from datetime import datetime
from prettytable import PrettyTable

# Function to get user input and clean it
def get_response():
    response = input("Enter your response = ")
    response = response.strip()
    return response

# Function to validate user input for menu selection
def validate_response(response: str):
    try:
        # Check if the input is an integer and within the valid options
        if int(response) in [1, 2, 3, 4]:
            return False  # Input is valid
        else:
            print("Please Enter a valid response")
            return True
    except ValueError:
        print("Please Enter a valid response")
        return True

# Function to register a new account
def register(account_name):
    # Create a balance file initialized to 0
    with open(f"{account_name}_balance.txt", "w") as file:
        file.write("0")

    # Create a transaction history file with headers
    with open(f"{account_name}_records.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "operation", "amount"])
        writer.writeheader()

    return

# Function to display a welcome message and options to the user
def welcome_user(acc_name, amount):
    print("\n----------------------------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"\nWelcome {acc_name}!")
    print(f"Your Account Currently Has -> ${amount}")
    print("You can perform the following operations ->")
    print("\nChoose your option ->\n")
    print("1  ->  Withdraw Money")
    print("2  ->  Deposit Money")
    print("3  ->  View Transaction History")
    print("4  ->  Log Out\n")
    return

# Function to handle money withdrawal and update records
def withdraw(acc_name, withdraw, balance):
    # Update the balance file
    with open(f"{acc_name}_balance.txt", "w") as file:
        file.write(f"{balance}")

    # Log the withdrawal transaction
    data = [f"{datetime.now()}", "Withdraw", f"{withdraw}"]
    with open(f"{acc_name}_records.csv", "a") as file:
        writer_object = csv.writer(file)
        writer_object.writerow(data)

    return

# Function to handle money deposit and update records
def deposit(acc_name, deposit, balance):
    # Update the balance file
    with open(f"{acc_name}_balance.txt", "w") as file:
        file.write(f"{balance}")

    # Log the deposit transaction
    data = [f"{datetime.now()}", "Deposit", f"{deposit}"]
    with open(f"{acc_name}_records.csv", "a") as file:
        writer_object = csv.writer(file)
        writer_object.writerow(data)

    return

# Main function to control the flow of the program
def main():
    print("\n----------------------------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print("\nPersonal Finance Tracker")
    print("\nChoose your option ->\n")
    print("1  ->  Login into your account")
    print("2  ->  Exit\n")

    response = get_response()

    # Validate initial user response
    while validate_response(response):
        response = get_response()

    if response == "1":
        acc_name = input("\nEnter your Account Name = ")

        while True:
            try:
                # Check if the account balance file exists and read the balance
                with open(f"{acc_name}_balance.txt") as file:
                    amount = int(file.readline())

                # Display options to the user
                welcome_user(acc_name, amount)

                response = get_response()

                while validate_response(response):
                    response = get_response()

                # Handle user choices
                if response == "1":
                    flag = True
                    while(flag):
                        try:
                            amount_to_withdraw = int(input("Enter Amount to withdraw ->"))
                            flag = False
                        except ValueError:
                            print("Please enter a Valid Amount.")
                            flag = True

                    new_amount = amount - amount_to_withdraw
                    if new_amount < 0:
                        sys.exit("You don't have enought money in your account.")
                    withdraw(acc_name, amount_to_withdraw, new_amount)

                elif response == "2":
                    flag = True
                    while(flag):
                        try:
                            amount_to_deposit = int(input("Enter Amount to deposit ->"))
                            print("Please enter a Valid Amount.")
                            flag = False
                        except ValueError:
                            flag = True


                    new_amount = amount + amount_to_deposit
                    deposit(acc_name, amount_to_deposit, new_amount)

                elif response == "3":
                    # Display transaction history
                    with open(f"{acc_name}_records.csv") as file:
                        reader = csv.reader(file)
                        next(reader, None)  # Skip header
                        print("\n\nThe Records are Shown Below:\n")
                        myTable = PrettyTable(["DateTime", "Operation", "Amount"])

                        for row in reader:
                            myTable.add_row(row)

                        print(myTable)

                elif response == "4":
                    sys.exit("*** The Program has Terminated... ***")

            except FileNotFoundError:
                # Handle the case where the account doesn't exist
                print("\nYou do not have an account.")
                print("Would you like to make an account")
                print("\nChoose your option ->\n")
                print("1  ->  Hell Yeahh")
                print("2  ->  Exit\n")

                response = get_response()

                while validate_response(response):
                    response = get_response()

                if response == "1":
                    # Register a new account
                    register(acc_name)
                    print("Congrats! Your account has been created successfully.....")
                    main()

                elif response == "2":
                    sys.exit("*** The Program has Terminated... ***")

    elif response == "2":
        sys.exit("***The Program has Terminated... ***")

if __name__ == "__main__":
    main()
