# Create a Customer class
class Customer:
  def __init__(first_name, last_name, username, password):
    self. first_name = first_name
    self. last_name = last_name
    self. usernmae = username
    self. Password = password

# Create a dictionary
existing_costumers = [
    Customer ( "first_name" == "Jane", "last_name"== "Cooper", "username"== "Jane_Cooper", "password"== "password000" ),
    Customer ("first_name" == "Mike", "last_name" == "Frank", "username" == "Mike_Frank", "password" == "password111" )
]
# Adding two new customers
existing_customers.append = ("first_name" == "David", "last_name" == "Sharon", "username" == " David_Sharon", "password" == "password222" ) 
existing_customers.append = ("first_name" == "Eve", "last_name" == "Bron", "username" == "Eve_Baron", "password" == "password333" )
print(existing_customers)

# ... (previous code for Signup class and customers dictionary)

def sign_in(customers):
  attempts = 0
  while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in customers and "password" in customers[username] and customers[username]["password"] == password:
      print("Welcome back, {}!".format(customers[username]["name"]))
      
      break
    else:
      attempts += 1
      print("Invalid credentials. {} attempts remaining.".format(5 - attempts))
    else:
    print("Too many failed attempts. Account locked.")

sign_in()

class Bank:
    def __init__(self):
        self.balance = 1000
        self.total_deposits = 0
        self.total_withdrawals = 0

    def transactions(self, initial_balance, deposit, withdraw, total_deposits, total_withdrawals):
        self.balance = initial_balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.total_deposits = total_deposits
        self.total_withdrawals = total_withdrawals

        # Banking options
        while True:
            print("\nBanking Options:")
            print("[1] Show Balance")
            print("[2] Deposit")
            print("[3] Withdrawal")
            print("[4] Print Statement")
            print("[5] Email Statement")
            print("[6] Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_balance()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                self.print_statement()
            elif choice == '5':
                self.email_statement()
            elif choice == '6':
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_balance(self):
        print("Your current balance is: $", self.balance)

    def deposit_money(self):
        amount = float(input("Enter amount to deposit: $"))
        self.balance += amount
        self.total_deposits += amount
        print("Deposit successful. Your new balance is: $", self.balance)

    def withdraw_money(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= self.balance:
            self.balance -= amount
            self.total_withdrawals += amount
            print("Withdrawal successful. Your new balance is: $", self.balance)
        else:
            print("Insufficient funds.")

    def print_statement(self):
        print("\nAccount Statement:")
        print("Initial Balance: $", self.initial_balance)
        print("Total Deposits: $", self.total_deposits)
        print("Total Withdrawals: $", self.total_withdrawals)
        print("Current Balance: $", self.balance)

    def email_statement(self):
        # You would need to implement email functionality here
        print("This feature is not yet implemented.")