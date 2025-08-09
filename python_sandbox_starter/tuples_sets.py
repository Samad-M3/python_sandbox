# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# A single value in a tuple needs a trailing comma
fruits2 = ("Banana",)
# print(fruit, type(fruit))

# Get value 
# print(fruits[2])

# Can't change value
# fruits[0] = "Pears"

# Delete tuple 
# del fruits

# Get length of tuple
# print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set 
months = {"May", "June", "April"}

# Check if something is in a set
# print("April" in months)

# Add to set 
months.add("July")

# Remove from set 
months.remove("April")

# Clear set
months.clear() 

# Delete set
# del months

print(months)
