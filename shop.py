class ThreeFailedAttempts(Exception):
    pass

def purchased(item, balance, prices):
    return balance >= prices.get(item, 0)

def goodbye_greeting(item):
    print(f"Here is your {item}!\n")
    print("Thanks for coming to The Store. Come again!")
    print("*******************************************")
    exit(0)

def retry_purchase(item, balance, prices, attempts=1):
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

    if purchased(item, balance, prices):
        goodbye_greeting(item)
    else:
        attempts += 1
        retry_purchase(item, balance, prices, attempts)

def greeting():
    prices = {"Phone": 300, "Watch": 50, "Belt": 25}
    balance = 100

    print("Welcome to The Store!")
    print("We currently have the following items:")
    for item, price in prices.items():
        print(f"{item} - £{price}")

    choice = input("\nWould you like to buy anything? (Enter 'exit' to exit the shop) ")

    if choice == "exit":
        print("Exiting store.")
        exit(0)
    elif choice in prices:
        try:
            if purchased(choice, balance, prices):
                goodbye_greeting(choice)
            else:
                retry_purchase(choice, balance, prices)
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
