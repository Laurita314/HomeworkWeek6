prices = {"Phone": 300, "Watch": 50, "Belt": 25}
balance = 100

class ThreeFailedAttempts(Exception):
    pass

def purchased(item, balance):
    if balance >= prices.get(item):
        return True
    else:
        return False

def goodbye_greeting(item):
    print(f"Here is your {item}!\n")
    print("Thanks for coming to The Store. Come again!")
    print("*******************************************")
    exit(0)

def retry_purchase(item, balance, attempts=1):
    if attempts == 3:
        raise ThreeFailedAttempts("Payment failed 3 times. Please exit the store.")
    more_money = input("Sorry, your payment failed. Do you have any more money? (Y/N)")
    if more_money.upper() == "Y":
        try:
            additional_amount = float(input("How much? "))
            balance += additional_amount
        except ValueError:
            print("Invalid input. Exiting store.")
            exit(1)
    else:
        print("Exiting store.")
        exit(0)

    if purchased(item, balance):
        goodbye_greeting(item)
    else:
        attempts += 1
        retry_purchase(item, balance, attempts)


def greeting():
    print("Welcome to The Store!")
    print("We currently have the following items:")
    for item in prices:
        print(f"{item} - £{prices.get(item)}")

    choice = input("\nWould you like to buy anything? (Enter 'exit' to exit the shop) ")

    if choice == "exit":
        print("Exiting store.")
        exit(0)
    elif choice in prices.keys():
        try:
            if purchased(choice, balance):
                goodbye_greeting(choice)
            else:
                retry_purchase(choice, balance)
        except ThreeFailedAttempts as e:
            print(e)
            exit(1)
    else:
        raise ValueError("Not a valid answer. Please return and try again.")

try:
    greeting()
except ValueError as e:
    print(e)
    exit(1)
