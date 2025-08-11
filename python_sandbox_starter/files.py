# Python has functions for creating, reading, updating, and deleting files.

# Open a file 
myFile = open("myFile.txt", "w")

# Get some infomation about the file that was just created
print("Name: ", myFile.name)
print("Is Closed: ", myFile.closed)
print("Opening Mode: ", myFile.mode)

# Write to file
myFile.write("I love playing tennis")
myFile.write(" and football on some occasions.")
myFile.close()

# Append to file 
myFile = open("myFile.txt", "a")
myFile.write(" I also am currently learning Python")
myFile.close()

# Read from file 
myFile = open("myFile.txt", "r+")
text = myFile.read(100)
print(text)