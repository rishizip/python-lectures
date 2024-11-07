# create a bank account class with 2 atributes - balance and account no.
# create methods for debit, credit and printing the balance


class Account:
    def __init__(self, bal, no):
        self.balance = bal
        self.account_no = no

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Rs", amount, "is debited")
            print("Total value =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "is credited")
        print("Total value =", self.get_balance())

    def get_balance(self):
        return self.balance

def main():
    account_no = int(input("Enter your account number: "))
    initial_balance = int(input("Enter your initial balance: "))

    acc1 = Account(initial_balance, account_no)

    print("Your Bank Balance is :", acc1.balance)
    print("Your account no is :", acc1.account_no)

    while True:
        print("\nChoose an option:")
        print("1. Debit")
        print("2. Credit")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter the amount to debit : "))
            acc1.debit(amount)
        elif choice == 2:
            amount = int(input("Enter the amount to credit : "))
            acc1.credit(amount)
        elif choice == 3:
            print("Your current balance is :", acc1.get_balance())
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()