print("Welcome to ATM")

class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceInquiry (self):  
        print("your balance is: 500")

    def cashWidthDrawal(self, amount):
        newAmount = 500-amount
        print("you withdrawed: " + str(amount) + " your remaining balance is: " + str(newAmount))

def main():
        name = input("Hello what is you name?")
        print("Hello, " + name)
        cardnumber = input("insert your card number: ")
        pin = input("Enter your pin: ")
        newUser = Atm(cardnumber, pin)

        print("Choose you activity")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("enter activity choice: "))

        if (activity == 1):
            newUser.balanceInquiry()
        elif (activity == 2):
            amount = int(input("Enter the amount: "))
            newUser.cashWidthDrawal(amount)
        else:
            print("enter a valid number")

if __name__ == "__main__":
    main()