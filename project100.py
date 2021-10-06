class atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def balanceEnquiry(self):
        print("Your balance is 563412")
    def withdrawal(self,amount):
        newAmount = 563412 - amount
        print("You have withdrawn"+str(amount)+"your remaining balance is"+str(newAmount))
def main():
    cardNumber = input("Enter your card number")       
    pinNumber = input("Enter your pin number")      
    atm1 = atm(cardNumber,pinNumber)
    print("Enter your choice")
    print("1.balance enquiry 2. Withdrawal")
    activity = int(input("enter 1 or 2"))
    if activity ==1:
        atm1.balanceEnquiry()
    elif activity ==2:
        amount = int(input("Enter the amount you want to withdraw"))
        atm1.withdrawal(amount)
    else:
        print("Enter a valid number")
if __name__ =="__main__":
    main()                 
