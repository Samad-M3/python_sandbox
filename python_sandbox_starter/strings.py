# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "samad"
age = 20
sport = "football"

# Concatenate
# print("Hi, my name is " + name + " and my age is " + str(age)) 

# String formatting

# Arguemnts by position 
# print("My name is {name} and I am {age}".format(name=name, age = age))

# F-Strings 
# print(f'Hi, my name is {name}, my age is {age} and my favourite sport is {sport}')

# String Methods

s = "fantasyfootball"

# Capitalise the first letter in the string
# print(s.capitalize())

# Make all uppercase 
# print(s.upper())

# Make all lowercase 
# print(s.lower())

# Swap case (switches the casing depending on what input was given)
# print(s.swapcase())

# Get length
# print(len(s))

# Replace (replaces the occurence of a letter/string with something else)
# print(s.replace("a", "i"))

# Count 
# print(s.count("f"))

# Starts with 
# print(s.startswith("fanta"))

# Ends with 
# print(s.endswith("tall"))

# Split into a list
# print(s.split())

# Find position of the first occurence of a letter
# print(s.find("a"))

# Is all alphanumeric 
# print(s.isalnum())

# Is all alphabetic 
# print(s.isalpha())

# Is all numeric
# print(s.isnumeric())