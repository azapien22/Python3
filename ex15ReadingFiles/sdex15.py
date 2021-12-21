# Ex. 15 Reading Files

# It means “from the module sys, import the function or parameter argv”.
# The sys module contains all kinds of system-related functions and constants.
# The argv parameter returns the specific way the script was called (e.g. from a command line interface).
from sys import argv

# Get argv command line arguments (When running the file) and assigning it 2 variables
script, filename = argv

# Open the file (Using the filename) and assign to a variable 
txt = open(filename)

# Print out the filename and print out the content of the opened file, using read()
print(f"Here's your {filename}:")
print(txt.read())
# Close File --- so as not to take up much computer memory
txt.close()

# Print out instructions and ask for user input using input()
print("Type the filename again:")
file_again = input("> ")

# Open the file (using the filename) and assign to a variable
txt_again = open(file_again)

# Print out the content of the opened file, using read()
print(txt_again.read())
# Close File --- so as not to take up much computer memory
txt_again.close()