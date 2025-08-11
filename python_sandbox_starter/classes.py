# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"
    
    def increase_age(self):
        self.age += 1

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"

# Init user object
user = User("Samad", "samad@gmail.com", 20)

user.increase_age()
# print(user.greeting())

# Init customer object 
customer = Customer("Jane Smith", "jane@outlook.com", "23")
customer.set_balance(400)
print(customer.greeting())
