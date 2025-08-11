# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict 
person = {
    "first_name": "Bob",
    "last_name": "John",
    "age": 40
}

# Use a constructor
person2 = dict(first_name="Neco", last_name="Williams", age=32)

# Get value
# print(person["first_name"])
# print(person2.get("last_name"))

# Add key/value
person["phone_number"] = "111-111-111"

# Get dict keys
# print(person.keys())

# Get dict values
# print(person.values())

# Get dict items
# print(person.items())

# Copy dict 
person3 = person.copy()
person3["school"] = "Havard"

# Remove item 
del(person["first_name"])
person.pop("age")

# Clear
person.clear()

# Get length 
# print(len(person3))

# List of dict
people = [
    {"name": "Smith", "age": 12},
    {"name": "Sarah", "age": 32},
    {"name": "Bob", "age": 23}
]

print(people[2]["name"])