# Create a Customer class
class Customer:
  def __init__(first_name, last_name, username, password):
    self. first_name = first_name
    self. last_name = last_name
    self. usernmae = username
    self. Password = password

# Create a dictionary
existing_costumers = [
    Customer ( "first_name" = "Jane", "last_name"= "Cooper", "username"= "Jane_Cooper", "password"= "password000" ),
    Customer ("first_name" = "Mike", "last_name" = "Frank", "username" = "Mike_Frank", "password" = "password111" )
]
# Adding two new customers
existing_customers.append = ("first_name" = "David", "last_name" = "Sharon", "username" = " David_Sharon", "password" = "password222" ) 
existing_customers.append = ("first_name" = "Eve", "last_name" = "Bron", "username" = "Eve_Baron", "password" = "password333" )
print(existing_customers)

# Create a Singup class
class Signup:
    def__init__(self):
    self.customers = {}
  def new_user(self):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = self.password()

  def password(self):
    while True:
      password = input("Create a password (between 6 and 12 characters, containing at least one lowercase letter): ")
      if 6 <= len(password) <= 12 and any(c.islower() for c in password):
        print("Password created successfully!")
        break
      else:
        print("Invalid password. Please try again.")

# Create an instance of the Signup class
signup = Signup()

# Start the signup process
signup.new_user()