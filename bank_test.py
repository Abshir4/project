import random
from shoping_map import the_shop



class Account:

    # Construct an Account object
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def getPin(self):
        return self.pin

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def bank():


    # Creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 1000)
        accounts.append(account)

    # ATM Processes
    while True:

        # Reading id from user
        id = int(input("\nEnter account pin: "))

        # Loop till id is valid
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Id.. Re-enter: "))

        # Iterating over account session
        while True:

            # Printing menu
            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")

            # Reading selection
            selection = int(input("\nEnter your selection: "))

            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getPin() == id:
                    accountObj = acc
                    break

            # View Balance
            if selection == 1:
                # Printing balance
                print(accountObj.getBalance())

            # Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")

                if ver_withdraw == "Yes".lower():
                    print("Verify withdraw")
                else:
                    break

                if amt < accountObj.getBalance():
                    # Calling withdraw method
                    accountObj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + "$")
                else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " n")
                    print("\nPlease make a deposit.")

            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount" + str(amt) + "$ Yes, or No ?\n")

                if ver_deposit == "Yes".lower():
                    # Calling deposit method
                    accountObj.deposit(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + "$\n")
                else:
                    break

            elif selection == 4:
                print("\nTransaction is now complete.")
                print("\nTransaction number: ", random.randint(10000, 1000000))
                print("\nThanks for choosing us as your bank\n")
                return main()

            # Any other choice
            else:
                print("That's an invalid choice.")


def main():

    row = 0
    col = 2
    running = True

    while running:
        print("You are now in", the_shop[row][col]['description'])
        print("You can go", the_shop[row][col]['exits'])

        command = input("> ")
        go = command.split()
        if (command == "ATM" and [row][col][0,2]):
            bank()

            if go[0].lower() == "go":
                if go[1].lower() in the_shop[row][col]['exits']:
                    if go[1].lower() == "north":
                        row -= 1
                    elif go[1].lower() == "south":
                        row += 1
                    elif go[1].lower() == "east":
                        col += 1
                    elif go[1].lower() == "west":
                        col -= 1

                    else:
                        print("You can't go in that direction.")
            elif go[0].lower() == "quit":
                running = False
            else:
                print("I don't understand", go[0])

if __name__ == '__main__':
    main()