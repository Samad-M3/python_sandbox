# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime 
from datetime import date
from datetime import datetime
import time 
from time import time 

# Import custom module 
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

dt_object = datetime.fromtimestamp(timestamp)

email = "yahoo890@gmail.com"
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")

# print(dt_object)


